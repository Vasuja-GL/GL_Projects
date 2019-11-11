"""Module for Verifying Discovery page
   File: Discovery_page.py
   Author: Vasuja
"""

import time
from collections import defaultdict

import web_wrappers.selenium_wrappers as base
import inspect

__author__ = "Vasuja"


class Discovery_page(object):

    def __init__(self, browser):
        self._browser = browser
        self.action_ele = base.WebElementAction(self._browser)
        self.INDEX = 1

    # def select_show_and_return_title(self, params):
    #     """
    #     `Description:` To select any show
    #
    #     `:param` params: name of the show which need to be Selected
    #
    #     `:return:` show_list, status
    #
    #     `Created by:` Vasuja K
    #     """
    #     status = True
    #     show_list = []
    #     params = defaultdict(lambda: '', params)
    #     try:
    #         show_with_xpath = {"APOLLO": "img_apollo", "SAVAGE_BUILDS": "img_savage_builds", "SERENGETI": "img_serengeti" }
    #         for key, value in show_with_xpath.items():
    #             if params["show_name"] == key:
    #                 #self.action_ele.explicit_wait(value, 40)
    #                 self.action_ele.mouse_hover(value)
    #                 time.sleep(1)
    #                 show_img = self._browser.element_finder(value)
    #                 self.action_ele.click_element(value)
    #                 show_list.append(str(show_img))
    #     except Exception as e:
    #         print(e)
    #         status = False
    #         self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
    #     return show_list, status
