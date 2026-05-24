# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""CSL styles exceptions."""

from __future__ import absolute_import, print_function


class StyleNotFoundError(Exception):
    """Style not found error."""


class StyleDependencyError(Exception):
    """Style dependency error."""
