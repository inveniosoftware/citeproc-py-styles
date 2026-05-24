#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2015-2021 CERN.
# SPDX-License-Identifier: MIT

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m check_manifest --ignore ".*-requirements.txt"
python -m pytest
