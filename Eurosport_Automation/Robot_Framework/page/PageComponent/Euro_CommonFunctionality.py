"""Module for execution of common portal functionalities such as login, log out, etc
   File: Disc_CommonFunctionality.py
   Author: Vasuja
"""

import os
import sys
import time, re
import inspect
from collections import defaultdict

import web_wrappers.selenium_wrappers as base

from log import log
from mapMgr import mapMgr
mapMgr.create_maplist("Eurosports")
mapDict = mapMgr.getMapDict()
mapList = mapMgr.getMapKeyList()

__author__ = "Vasuja"

_RETRY_COUNT = 3

Initial_Login = False


class Euro_CommonFunctionality(object):

    def __init__(self, browser):
        self._browser = browser
        self.action_ele = base.WebElementAction(self._browser)
        self.Initial_Login = False

    def open_url(self, url):
        """
        `Description:` To open Any portal.

        `:param` url: URL of Eurosport Page

        `:return:`

        `Created by:` Vasuja K
        """
        try:
            self._browser.go_to(url)
            log.mjLog.LogReporter("Euro_CommonFunctionality", "info", "Open URL successful")
        except Exception as err:
            print(err.message)
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
            raise Exception("Open URL is failed !!")

    def euro_login(self, params):
        """
        `Description:` Login for Eurosport portal

        `:params` Dictionary contains login details

        `:return:` status - True/False

        `Created by:` Vasuja K
        """
        try:
            params = defaultdict(lambda: None, params)
            # import pdb;
            # pdb.Pdb(stdout=sys.__stdout__).set_trace()
            status = True
            if params["cookie_policy"]:
                self.action_ele.click_element("Global_EuroSport_Cookie_Policy_Accept_Button_xpath")
            self.action_ele.click_element("Global_EuroSport_Sign_In_Link_xpath")

            # self.action_ele.clear_input_text("Global_EuroSport_locator_Discovery_Email_ID_css")
            # self.action_ele.clear_input_text("Global_EuroSport_Discovery_Password_css")
            self.action_ele.input_text("Global_EuroSport_locator_Discovery_Email_ID_css", params["Username"])
            self.action_ele.input_text("Global_EuroSport_Discovery_Password_css", params["Password"])
            self.action_ele.explicit_wait("Global_Eurosport_Sign_In_Button_xpath")
            self.action_ele.click_element("Global_Eurosport_Sign_In_Button_xpath")
            self.action_ele.explicit_wait("Global_EuroSport_Account")

        except Exception as err:
            status = False
            print(err.message)
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
            raise Exception("Login failed   !!")
        return status

    def close_browser(self):
        """
        `Description:` Close the browser object

        `:param` driver: WebDriver object

        `:return:``

        `Created by:`
        """
        try:
            self._browser.quit()
        except Exception as err:
            print(err.message)
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
            raise Exception("Failed to close browser!!")

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


    def switch_page_OnDemand(self, *options):
        """
        `Description:` Switch to See All Shows page

        `Param:`  None

        `Returns:` None

        `Created by:` Vasuja K
        """
        try:
            self.action_ele.explicit_wait("EuroSport_on_demand")

            self.action_ele.click_element('EuroSport_on_demand')

        except Exception as err:
            print(err.message)
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
            raise Exception("Switch to OnDemand page failed!!")
