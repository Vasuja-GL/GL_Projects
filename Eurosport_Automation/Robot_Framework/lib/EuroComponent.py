"""Module for Discovery portal functionalities
"""
import time
import stafenv
import sys

from web_wrappers.selenium_wrappers import LocalBrowser
from page.EuroComponent import EuroPage


class EuroComponent():
    ''' Discovery Component Interface to interact with the ROBOT keywords
    '''

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, **params):
        self.browsertype = params.get('browser', 'chrome').lower()
        self.profile_path = params.get('profile_path', '').lower()
        self._browser = LocalBrowser(self.browsertype, self.profile_path)
        browser_obj = self._browser.get_current_browser()
        browser_obj.maximize_window()
        self.euro_page = EuroPage(self._browser)

    def open_url(self,url):
        """
        `Description:` This function is used to open Discovery portal page

        `:param1` url: URL of Discovery page

        `:return:` None

        `Created by:`
        """
        try:
            self.euro_page.common_fun.open_url(url)
        except Exception as e:
            print(e)

    def euro_login(self, **params):
        """
        `Description:` Login for Eurosport portal

        `:params` Dictionary contains login details

        `:return:` status - True/False

        `Created by:` Vasuja K
        """
        try:
            status = self.euro_page.common_fun.euro_login(params)
            return status
        except:
            raise AssertionError("Login Failed!!")

    def switch_page(self, **params):
        """
        `Description:` Switch any page

        `:param` params: name of the page which need to be switched

        `:return:` None

        `Created by:` Vasuja K
        """
        try:
            print("IN MAIN:")
            if params.keys():
                self.euro_page.common_fun.switch_page(**params)
            else:
                print("Please check that the input parameters have been provided",
                        self.switch_page.__doc__)
        except:
            raise AssertionError("Page Switch Failed!!")

    def close_the_browser(self, **params):
        """
        `Description:` Close the browser object

        `:param` driver: WebDriver object

        `:return:` None

        `Created by:`
        """
        try:
            time.sleep(2)
            self.euro_page.common_fun.close_browser()
        except:
            raise AssertionError("Close browser Failed!!")

    def play_video(self, **params):
        """
        `Description:` To play any video

        `:params` Dictionary contains video details

        `:return:` status - True/False

        `Created by:` Vasuja K
        """
        try:
            status = self.euro_page.on_demand.play_video(params)
            return status
        except:
            raise AssertionError("Failed to play video!!")




