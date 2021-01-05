Pigment
=======

**Pigment** is a set of Python utilities for colors.

.. code:: python

    >>> red = Color(255, 0, 0)
    >>> blue = Color(0, 0, 255)
    >>> blend(red, blue).hsv
    (300, 100, 50)

.. image:: https://pepy.tech/badge/pigment
   :target: https://pepy.tech/project/pigment
   :alt: Downloads
.. image:: https://img.shields.io/pypi/pyversions/pigment
   :target: https://pypi.org/project/pigment
   :alt: Supported Versions
.. image:: https://img.shields.io/github/workflow/status/bsoyka/pigment/Testing%20with%20pytest?label=tests
   :target: https://github.com/bsoyka/pigment/actions?query=workflow%3A%22Testing+with+pytest%22
   :alt: Testing
.. image:: https://img.shields.io/pypi/l/pigment
   :target: https://github.com/bsoyka/pigment/blob/master/LICENSE
   :alt: License
.. image:: https://img.shields.io/pypi/v/pigment?label=latest
   :target: https://pypi.org/project/pigment
   :alt: Version

Installation
------------

Pigment is available on PyPI:

.. code:: console

    $ python -m pip install pigment

Pigment officially supports Python 3.5+.

Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2

   reference
   exceptions
