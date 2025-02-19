.. Copyright 2014 splinter authors. All rights reserved.
   Use of this source code is governed by a BSD-style
   license that can be found in the LICENSE file.

.. meta::
    :description: How to use splinter with Flask.
    :keywords: splinter, python, tutorial, how to install, installation, Flask

+++++
Flask
+++++

Dependencies
------------

.. module:: splinter.driver.flaskclient

To use the ``flask`` driver, the following must be installed:

`Flask <https://pypi.python.org/pypi/Flask>`_,
`lxml <https://pypi.python.org/pypi/lxml>`_,
`cssselect <http://pypi.python.org/pypi/cssselect>`_.

When splinter is installed via pip, the `flask` extra argument can be provided.
This will automatically install Flask.

.. code-block:: bash

    python -m pip install splinter[flask]

Usage
-----

To use the ``flask`` driver, you'll need to pass the string ``flask`` and an app instances via the
``app`` keyword argument when you create the ``Browser`` instance:

.. code-block:: python

    from cksplinter import Browser
    browser = Browser('flask', app=app)

**Note:** if you don't provide any driver to ``Browser`` function, ``firefox`` will be used.

When visiting pages with the Flask client, you only need to provide a path rather than a full URL.
For example:

.. code-block:: python

    browser.visit('/my-path')

API docs
--------

.. autoclass:: splinter.driver.flaskclient.FlaskClient
   :members:
   :inherited-members:
   :exclude-members: execute_script, evaluate_script
