# -*- coding: utf-8 -*-
#
# This file is part of citeproc-py-styles.
# Copyright (C) 2016 CERN.
#
# citeproc-py-styles is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# citeproc-py-styles is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with citeproc-py-styles; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""citeproc-py-styles module tests."""

from __future__ import absolute_import, print_function

import os

import pytest
from citeproc_styles import get_style_filepath, get_style_name
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
