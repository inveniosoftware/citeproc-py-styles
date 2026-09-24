# SPDX-FileCopyrightText: 2016-2018 CERN.
# SPDX-License-Identifier: MIT

"""CSL styles exceptions."""


class StyleNotFoundError(Exception):
    """Style not found error."""


class StyleDependencyError(Exception):
    """Style dependency error."""
