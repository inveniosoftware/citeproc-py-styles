#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# This file is part of citeproc-py-styles.
# Copyright (C) 2019 CERN.
#
# citeproc-py-styles is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
# Update the git submodule. If there are updates, create and tag a new release.
set -e

# Setup the Git credentials for committing and tagging as Invenio.
setup_git () {
    git config user.name "Invenio"
    git config user.email "info@inveniosoftware.org"
}

# Commit changes in the git submodule.
commit_changes () {
    git add citeproc_styles/version.py
    git commit -am "data: update the CSL styles in build $TRAVIS_BUILD_NUMBER"
}

# Create a new version by changing the version number
# and creating a tagged commit.
tag_release () {
    sed -i "s/__version__ =.*/__version__ = '$VERSION'/" citeproc_styles/version.py
    git add citeproc_styles/version.py
    git commit -m "release: $VERSION"
    git tag -a $TAG -m "release: citeproc_py_styles $VERSION"
}

# In case we run the script locally we have to set the build number.
if [ -z "$TRAVIS_BUILD_NUMBER" ]; then TRAVIS_BUILD_NUMBER="local"; fi

# Update the git submodule to add upstream changes. If there are changes
# we prepare a new release by commiting the upstream changes and tagging
# a new release using a YYYY.MM.DD schema.
git submodule update --remote --merge
VERSION="$(date +'%Y.%m.%d')"
TAG="v$VERSION"
if [ -z "$(git diff --name-only)" ]
then
    echo "No changes found."
elif [ "$(git tag list $TAG)" ]
then
    echo "Tag $TAG already exists"
    exit 1
else
    echo "Changes found. Commiting and tagging $VERSION."
    setup_git
    commit_changes
    tag_release
fi
