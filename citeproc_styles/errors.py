# -*- coding: utf-8 -*-
#
# This file is part of citeproc-py-styles.
# Copyright (C) 2016-2018 CERN.
#
# citeproc-py-styles is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""CSL styles exceptions."""

from __future__ import absolute_import, print_function


class StyleNotFoundError(Exception):
    """Style not found error."""


class StyleDependencyError(Exception):
    """Style dependency error."""
