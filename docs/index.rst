==================
citeproc-py-styles
==================

About
=====
This module is meant to be used as a static resources package,
in order to make it easy to include the required Citation Style
files (.csl) when using citeproc-py.
In order to avoid always installing ~40MB of files each time you
include it in a project you could specify it as an extra in your
setup.py, and only use it in the production environment or as an
optional feature of your module. (Example setup.py)

The included files are originally hosted on the CSL Style Repository
which belongs to the CSL Project

Note: The style files are referenced as a git submodule. This means
that this repository/package is pinned on a specific commit of the CSL
Style Repository, and thus may not include any fixes or new styles that
may have been added. Next versions of this repository will of course
'bump' the styles version to the latest commit, but this will not happen
on a scheduled basis for the time being.


Table of contents
=================

.. toctree::
   :maxdepth: 1
   :numbered:

   installation


