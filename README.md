<!--
SPDX-FileCopyrightText: 2016-2018 CERN.
SPDX-License-Identifier: MIT
-->

# citeproc-py-styles

[![CI](https://github.com/inveniosoftware/citeproc-py-styles/workflows/CI/badge.svg)](https://github.com/inveniosoftware/citeproc-py-styles/actions?query=workflow%3ACI)
[![License](https://img.shields.io/github/license/inveniosoftware/invenio-app-rdm.svg)](https://github.com/inveniosoftware/invenio-app-rdm/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/citeproc-py-styles.svg)](https://pypi.org/pypi/citeproc-py-styles)

## About

This module is meant to be used as a static resources package, in order to make
it easy to include the required Citation Style files (.csl) when using
[citeproc-py](https://github.com/brechtm/citeproc-py).

In order to avoid always installing ~40MB of files each time you include it in
a project you could specify it as an extra in your `setup.py`, and only use it
in the production environment or as an optional feature of your module.
([Example setup.py](https://github.com/inveniosoftware/invenio-records-rest/blob/master/setup.py))

The included files are originally hosted on the
[CSL Style Repository](https://github.com/citation-style-language/styles) which
belongs to the [CSL Project](http://citationstyles.org/).

Note: The style files are referenced as a git submodule. This means that this
repository/package is pinned on a specific commit of the CSL Style Repository,
and thus may not include any fixes or new styles that may have been added.
Next versions of this repository will of course 'bump' the styles version to
the latest commit, but this will not happen on a scheduled basis for the time
being.

## Installation

citeproc-py-styles is on PyPI so all you need is:

```console
pip install citeproc-py-styles
```

## Usage

This is a minimal example of how one could use `citeproc-py-styles` to render a
citation with `citeproc-py`:

```python
from citeproc import (Citation, CitationItem, CitationStylesBibliography,
                      CitationStylesStyle, formatter)
from citeproc.source.json import CiteProcJSON
from citeproc_styles import get_style_filepath

csl_data = json.loads("...")
source = CiteProcJSON(csl_data)

style_path = get_style_filepath('apa')
style = CitationStylesStyle(style_path)

bib = CitationStylesBibliography(style, source, formatter.plain)
bib.register(Citation([CitationItem('data_id')]))
print(''.join(bib.bibliography()[0]))
```
