"""Module for Verifying On_Demand page
   File: On_Demand.py
   Author: Vasuja
"""

import time
import sys
from collections import defaultdict

import web_wrappers.selenium_wrappers as base
import inspect

__author__ = "Vasuja"


class On_Demand(object):

    def __init__(self, browser):
        self._browser = browser
        self.action_ele = base.WebElementAction(self._browser)
        self.INDEX = 1

    def play_video(self, params):
        """
        `Description:` To play any video

        `:params` Dictionary contains video details

        `:return:` status - True/False

        `Created by:` Vasuja K
        """
        status = True
        params = defaultdict(lambda: '', params)
        try:
            self.action_ele.explicit_wait(params["play_button_xpath"])
            self.action_ele.click_element(params["play_button_xpath"])
        except Exception as e:
            print(e)
            status = False
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
        return status
