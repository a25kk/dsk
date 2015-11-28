# dsk.sitecontent

## Sitecontent package containing folderish content pages

* `Source code @ GitHub <https://github.com/a25kk/dsk.sitecontent>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/dsk.sitecontent>`_
* `Documentation @ ReadTheDocs <http://dsksitecontent.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/a25kk/dsk.sitecontent>`_

## How it works

This package provides a Plone addon as an installable Python egg package.

The generated Python package hold the necessary scaffold to add content types
via the 'contenttype' template and to add functionality.

In order to get productive you still need to generate a contenttype

```bash
$ cd dsk.sitecontent/src/dsk/sitecontent/
$ mrbob --config ~/.mrbob.ini -O example_type bobtemplates:contenttype

```


## Installation

To install `dsk.sitecontent` you simply add ``dsk.sitecontent``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `dsk.sitecontent` using the Add-ons control panel.
