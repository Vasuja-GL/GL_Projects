"""Module for execution of common portal functionalities such as login, log out, etc
   File: Disc_CommonFunctionality.py
   Author: Vasuja
"""

import os
import sys
import time,re
import inspect
from collections import defaultdict

# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "utils"))

import web_wrappers.selenium_wrappers as base

from log import log
from mapMgr import mapMgr
mapMgr.create_maplist("Discovery")
mapDict = mapMgr.getMapDict()
mapList = mapMgr.getMapKeyList()

__author__ = "Vasuja"

_RETRY_COUNT = 3

Initial_Login = False


class Disc_CommonFunctionality(object):

    def __init__(self, browser):
        self._browser = browser
        self.action_ele = base.WebElementAction(self._browser)
        self.Initial_Login = False

    def open_url(self, url):
        """
        `Description:` To open Discovery portal.

        `:param` url: URL of Discovery Page

        `:return:`

        `Created by:` Vasuja K
        """
        self._browser.go_to(url)
        log.mjLog.LogReporter("Disc_CommonFunctionality", "info", "Open URL successful")

    def euro_login(self, params):
        """
        `Description:` Login for Eurosport portal

        `:params` Dictionary contains login details

        `:return:` status - True/False

        `Created by:` Vasuja K
        """
        try:
            params = defaultdict(lambda: None, params)
            import pdb;
            pdb.Pdb(stdout=sys.__stdout__).set_trace()
            status = True
            if params["cookie_policy"]:
                self.action_ele.click_element("Global_EuroSport_Cookie_Policy_Accept_Button_xpath")
            self.action_ele.click_element("Global_EuroSport_Sign_In_Link_xpath")

            # self.action_ele.clear_input_text("Global_EuroSport_locator_Discovery_Email_ID_css")
            # self.action_ele.clear_input_text("Global_EuroSport_Discovery_Password_css")
            self.action_ele.input_text("Global_EuroSport_locator_Discovery_Email_ID_css", params["Username"])
            self.action_ele.input_text("Global_EuroSport_Discovery_Password_css", params["Password"])
            self.action_ele.click_element("Global_Eurosport_Sign_In_Button_xpath")

        except Exception as err:
            print(err.message)
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
            raise Exception("Login failed!!")

    def close_browser(self):
        """
        `Description:` Close the browser object

        `:param` driver: WebDriver object

        `:return:``

        `Created by:` Vasuja K
        """
        # time.sleep(2)
        self._browser.quit()
        if self._browser.console_log:
            path = self._browser.console_log.name
            self._browser.console_log.close()
            os.unlink(path)
        self.Initial_Login = False

    def switch_page(self, **params):
        """
        `Description:` To switch to other pages based on given name

        `:param` params: page name which need to be switch

        `:return:`

        `Created by:` Vasuja K
        """
        try:
            print("IN COMMON SWITCH")
            print(params)
            getattr(self, "switch_page_" + params['page'])(params)
        except Exception as err:
            print(err.message)
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
            raise Exception("Switch page failed!!")

    def switch_page_see_all_shows(self, *options):
        """
        `Description:` Switch to See All Shows page

        `Param:`  None

        `Returns:` None

        `Created by:` Vasuja K
        """
        self.action_ele.explicit_wait("shows")
        self.action_ele.click_element('shows')
        # import pdb;
        # pdb.Pdb(stdout=sys.__stdout__).set_trace()
        self.action_ele.explicit_wait("see_all_shows")
        time.sleep(1)
        self.action_ele.mouse_hover('see_all_shows_link')
        self.action_ele.click_element("see_all_shows_link")
        self.action_ele.explicit_wait("tv_shows")

    def switch_page_my_vedios(self, *options):
        """
        `Description:` Switch to See my_vedios

        `Param:`  None

        `Returns:` None

        `Created by:` Vasuja K
        """
        self.action_ele.explicit_wait("dscHeaderMain__hideMobile")
        self.action_ele.click_element('dscHeaderMain__hideMobile')
        self.action_ele.explicit_wait("my_vedios")
        time.sleep(1)
        #self.action_ele.mouse_hover('my_vedios')
        self.action_ele.click_element("my_vedios")
        self.action_ele.explicit_wait("my_vedios_title")