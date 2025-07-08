# -*- coding: utf-8 -*-
#
# This file is part of citeproc-py-styles.
# Copyright (C) 2016-2018 CERN.
#
# citeproc-py-styles is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""CSL styles."""

from __future__ import absolute_import, print_function

import importlib.resources
import os
import sys

from lxml.etree import iterparse
from six import reraise as raise_

from .errors import StyleDependencyError, StyleNotFoundError
from .version import __version__

independent_dir = 'styles'
dependent_dir = 'styles/dependent'

xml_namespace = "http://purl.org/net/xbiblio/csl"


def _resolve_dependent_style(style_path):
    """Get the independent style of a dependent style.

    :param path style_path: Path to a dependent style.
    :returns: Name of the independent style of the passed dependent style.
    :raises: StyleDependencyError: If no style could be found/parsed.

    CSL Styles are split into two categories, Independent and Dependent.
    Independent styles, as their name says, are self-sustained and contain all
    the necessary information in order to format a citation. Dependent styles
    on the other hand, depend on Independent styles, and actually just pose as
    aliases for them. For example 'nature-digest' is a dependent style that
    just points to the 'nature' style.

    .. seealso::

        `CSL Specification
         <http://docs.citationstyles.org/en/stable/specification.html#file-types>`_
    """
    try:
        # The independent style is mentioned inside a link element of
        # the form 'http://www.stylesite.com/stylename'.
        for _, el in iterparse(style_path, tag='{%s}link' % xml_namespace):
            if el.attrib.get('rel') == 'independent-parent':
                url = el.attrib.get('href')
                return url.rsplit('/', 1)[1]
    except Exception:
        # Invalid XML, missing info, etc. Preserve the original exception.
        stacktrace = sys.exc_info()[2]
    else:
        stacktrace = None

    raise_(StyleDependencyError('Dependent style {0} could not be parsed'
                                .format(style_path)), None, stacktrace)


def _resource_exists(resource):
    """Tests if a resource exists within this package."""
    resource_path = importlib.resources.files("citeproc_styles") / resource
    return resource_path.is_file()


def _resource_filename(resource):
    """Get resource file name."""
    resource_path = importlib.resources.files("citeproc_styles") / resource
    with importlib.resources.as_file(resource_path) as f:
        # note: this will fail if the resource is not a file,
        # for example inside zip
        return str(f)


def _resource_listdir(resource):
    """List the contents of a resource directory."""
    resource_path = importlib.resources.files("citeproc_styles") / resource
    return [str(f) for f in resource_path.iterdir() if f.is_file()]


def get_style_filepath(style, resolve_dependencies=True):
    """Get the full path of a style file.

    :param style: The name of the style (eg. 'apa')
    :param resolve_dependencies: If True, for dependent styles the independent
                                 style is parsed and it's path is returned.
    :returns: Filepath of a .csl style file.
    """
    independent_style = os.path.join(independent_dir, '{0}.csl'.format(style))
    if _resource_exists(independent_style):
        return _resource_filename(independent_style)

    dependent_style = os.path.join(dependent_dir, '{0}.csl'.format(style))
    if _resource_exists(dependent_style):
        style_path = _resource_filename(dependent_style)

        if resolve_dependencies:
            inner_style = _resolve_dependent_style(style_path)
            inner_style = os.path.join(independent_dir,
                                       '{0}.csl'.format(inner_style))
            if _resource_exists(inner_style):
                return _resource_filename(inner_style)
            else:
                raise StyleNotFoundError(
                    'The independent style {0} was not found.'
                    .format(inner_style)
                )
        return style_path

    raise StyleNotFoundError('The style {0} was not found.'.format(style))


def get_style_name(style):
    """Get the proper name of a style.

    Example: For 'apa' this would be 'American Psychological Association 6th
    edition'.
    """
    try:
        filepath = get_style_filepath(style, resolve_dependencies=False)
        for _, el in iterparse(filepath, tag='{%s}title' % xml_namespace):
            return el.text
        else:
            return style
    except StyleNotFoundError:
        raise
    except Exception:
        # If the XML parsing goes wrong, just use the style's short name
        return style


def get_all_styles():
    """Get a dict of all the available styles and their long names.

    .. note::

        This function obviously takes a lot of time to execute. It would be
        a good practice for the result to be cached, and then reused.
    """
    styles = {}
    for styles_dir in (independent_dir, dependent_dir):
        style_files = (s for s in _resource_listdir(styles_dir)
                       if s.endswith('.csl'))
        style_names = (s.replace('.csl', '') for s in style_files)
        styles.update({s: get_style_name(s)
                       for s in style_names})
    return styles


__all__ = ('__version__', 'get_style_filepath', 'get_style_name',
           'get_all_styles')
