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

    def select_show_and_return_title(self, params):
        """
        `Description:` To select any show

        `:param` params: name of the show which need to be Selected

        `:return:` show_list, status

        `Created by:` Vasuja K
        """
        status = True
        show_list = []
        params = defaultdict(lambda: '', params)
        try:
            show_with_xpath = {"APOLLO": "img_apollo", "SAVAGE_BUILDS": "img_savage_builds", "SERENGETI": "img_serengeti" }
            for key, value in show_with_xpath.items():
                if params["show_name"] == key:
                    #self.action_ele.explicit_wait(value, 40)
                    self.action_ele.mouse_hover(value)
                    time.sleep(1)
                    show_img = self._browser.element_finder(value)
                    self.action_ele.click_element(value)
                    show_list.append(str(show_img))
        except Exception as e:
            print(e)
            status = False
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
        return show_list, status

    def verify_favorites_status(self):
        """
        `Description:` To verify Favorites status

        `:param` params:

        `:return:` status

        `Created by:` Vasuja K
        """
        status = True
        try:
            favorites_icon_plus = self._browser.element_finder("favorites_plus")
            if favorites_icon_plus:
                print ("favorites is not set and it is a + icon")
                self.action_ele.click_element("favorites_plus")
                if not self._browser.element_finder("favorites_minus"):
                    status = False
                    return status

            favorites_icon_minus = self._browser.element_finder("favorites_minus")
            if favorites_icon_minus:
                print ("favorites is already set and it is a - icon")
                self.action_ele.click_element("favorites_minus")
                if not self._browser.element_finder("favorites_plus"):
                    status = False
                    return status

        except Exception as e:
            print(e)
            status = False
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
        return status

    def add_show_to_favorite_list(self, params):
        """
        `Description:` To add show to favorite list

        `:param` params: None

        `:return:` status

        `Created by:` Vasuja K
        """
        status = True
        try:
            plus_icons = {"APOLLO": "apollo_favorites_plus", "SAVAGE_BUILDS": "savage_builds_favorites_plus", "SERENGETI": "serengethi_favorites_plus"}
            show_list = self.select_show_and_return_title(params)
            #show_title_list = show_title_list.append(show_list[0])
            for key, value in plus_icons.items():
                if params["show_name"] == key:
                    favorites_icon_plus = self._browser.element_finder(value)
                    if favorites_icon_plus:
                        print ("favorites is not set and it is a + icon")
                        self.action_ele.explicit_wait(value)
                        self.action_ele.click_element(value)
                        if not self._browser.element_finder("favorites_minus"):
                            status = False
                            return status

                    favorites_icon_minus = self._browser.element_finder("favorites_minus")
                    if favorites_icon_minus:
                        print ("favorites is already set and it is a - icon")
                        # self.action_ele.click_element("favorites_minus")
                        # if not self._browser.element_finder("favorites_plus"):
                    time.sleep(1)
        except Exception as e:
            print(e)
            status = False
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
        return show_list[0], status

    def verify_favorites_shows(self, params):
        """
        `Description:` To verify Favorites shows

        `:param` params:

        `:return:` status

        `Created by:` Vasuja K
        """
        status = False
        try:
            show_with_xpath = {"APOLLO": "img_apollo", "SAVAGE_BUILDS": "img_savage_builds2", "SERENGETI": "img_serengeti" }
            for key, value in show_with_xpath.items():
                if params["show_name"] == key:
                    if self.action_ele.explicit_wait(value):
                        print "Favorite show is verified"
                        status = True
        except Exception as e:
            print(e)
            self.action_ele.takeScreenshot(inspect.currentframe().f_code.co_name)
        return status