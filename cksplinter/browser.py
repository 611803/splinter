# -*- coding: utf-8 -*-

# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


import logging

from http.client import HTTPException

from urllib3.exceptions import MaxRetryError

from selenium.common.exceptions import WebDriverException

from cksplinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver
from cksplinter.driver.webdriver.remote import WebDriver as RemoteWebDriver
from cksplinter.driver.webdriver.chrome import WebDriver as ChromeWebDriver
from cksplinter.exceptions import DriverNotFoundError


_DRIVERS = {
    'chrome': None,
    'edge': None,
    'firefox': None,
    'remote': None,
    'django': None,
    'flask': None,
    'zope.testbrowser': None,
}

try:
    from cksplinter.driver.webdriver.chrome import WebDriver as ChromeWebDriver
    from cksplinter.driver.webdriver.firefox import WebDriver as FirefoxWebDriver
    from cksplinter.driver.webdriver.remote import WebDriver as RemoteWebDriver

    _DRIVERS['chrome'] = ChromeWebDriver
    _DRIVERS['firefox'] = FirefoxWebDriver
    _DRIVERS['remote'] = RemoteWebDriver
except ImportError as e:
    logging.debug(f'Import Warning: {e}')


try:
    from cksplinter.driver.webdriver.edge import WebDriver as EdgeWebDriver

    _DRIVERS["edge"] = EdgeWebDriver
except ImportError as e:
    logging.debug(f'Import Warning: {e}')


try:
    from cksplinter.driver.zopetestbrowser import ZopeTestBrowser

    _DRIVERS["zope.testbrowser"] = ZopeTestBrowser
except ImportError as e:
    logging.debug(f'Import Warning: {e}')

try:
    import django  # noqa
    from cksplinter.driver.djangoclient import DjangoClient

    _DRIVERS["django"] = DjangoClient
except ImportError as e:
    logging.debug(f'Import Warning: {e}')

try:
    import flask  # noqa
    from cksplinter.driver.flaskclient import FlaskClient

    _DRIVERS["flask"] = FlaskClient
except ImportError as e:
    logging.debug(f'Import Warning: {e}')


def get_driver(driver, retry_count=3, *args, **kwargs):
    """Try to instantiate the driver.

    Common selenium errors are caught and a retry attempt occurs.
    This can mitigate issues running on Remote WebDriver.

    """
    err = None

    for _ in range(retry_count):
        try:
            return driver(*args, **kwargs)
        except (IOError, HTTPException, WebDriverException, MaxRetryError) as e:
            err = e

    raise err


def Browser(driver_name="firefox", retry_count=3, *args, **kwargs):  # NOQA: N802
    """Get a new driver instance.

    Extra arguments will be sent to the driver instance.

    If there is no driver registered with the provided ``driver_name``, this
    function will raise a :class:`splinter.exceptions.DriverNotFoundError`
    exception.

    Arguments:
        driver_name (str): Name of the driver to use.
        retry_count (int): Number of times to try and instantiate the driver.

    Returns:
        Driver instance
    """

    try:
        driver = _DRIVERS[driver_name]
    except KeyError:
        raise DriverNotFoundError("No driver for %s" % driver_name)

    return get_driver(driver, retry_count=retry_count, *args, **kwargs)
