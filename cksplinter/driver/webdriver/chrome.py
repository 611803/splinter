# -*- coding: utf-8 -*-

# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from cksplinter.driver.webdriver import BaseWebDriver, WebDriverElement
from cksplinter.driver.webdriver.cookie_manager import CookieManager


class WebDriver(BaseWebDriver):

    driver_name = "Chrome"

    def __init__(
        self,
        options=None,
        user_agent=None,
        wait_time=2,
        fullscreen=False,
        incognito=False,
        headless=False,
        **kwargs
    ):

        options = options or Options()

        if user_agent is not None:
            options.add_argument("--user-agent=" + user_agent)

        if incognito:
            options.add_argument("--incognito")

        if fullscreen:
            options.add_argument("--kiosk")

        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

        driver = Chrome(options=options, **kwargs)

        super(WebDriver, self).__init__(driver, wait_time)
