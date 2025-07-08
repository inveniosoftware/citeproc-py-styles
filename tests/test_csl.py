# -*- coding: utf-8 -*-
#
# This file is part of citeproc-py-styles.
# Copyright (C) 2016-2018 CERN.
#
# citeproc-py-styles is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""citeproc-py-styles module tests."""

from __future__ import absolute_import, print_function

import os

import pytest

from citeproc_styles import get_all_styles, get_style_filepath, get_style_name
from citeproc_styles.errors import StyleNotFoundError


def test_style_filepath():
    """Test style filepath retrieval."""
    filepath = get_style_filepath('apa')
    assert os.path.exists(filepath)
    assert 'styles/apa.csl' in filepath

    filepath = get_style_filepath('nature-digest')
    assert os.path.exists(filepath)
    assert 'styles/nature.csl' in filepath

    filepath = get_style_filepath('nature-digest', resolve_dependencies=False)
    assert os.path.exists(filepath)
    assert 'styles/dependent/nature-digest.csl' in filepath

    with pytest.raises(StyleNotFoundError):
        filepath = get_style_filepath('non-existent-style')


def test_style_name():
    """Test style name retrieval."""
    name = get_style_name('apa')
    assert 'American Psychological Association' in name

    name = get_style_name('nature-digest')
    assert 'Nature Digest' in name

    with pytest.raises(StyleNotFoundError):
        name = get_style_name('non-existent-style')


def test_list_all_styles():
    """Test listing styles."""
    styles = get_all_styles()
    assert "Journal of Applied Animal Research" in styles.values()
