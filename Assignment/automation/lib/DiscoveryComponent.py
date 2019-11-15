"""Module for Discovery portal functionalities
"""
import time
import stafenv
import sys

from web_wrappers.selenium_wrappers import LocalBrowser
from page.DiscoveryComponent import DiscoveryPage

_DEFAULT_TIMEOUT = 3

class DiscoveryComponent():
    ''' Discovery Component Interface to interact with the ROBOT keywords
    '''

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, **params):
        self.browsertype = params.get('browser', 'chrome').lower()
        self._browser = LocalBrowser(self.browsertype)
        browser_obj = self._browser.get_current_browser()
        browser_obj.maximize_window()
        self.discovery_page = DiscoveryPage(self._browser)

    def close_and_reopen_browser(self):
        self._browser.quit()
        time.sleep(2)
        # open a new browser
        self._browser = LocalBrowser(self.browsertype)
        self._browser.get_current_browser().maximize_window()
        self.discovery_page = DiscoveryPage(self._browser)

    def open_url(self,url):
        """
        `Description:` This function is used to open Discovery portal page

        `:param1` url: URL of Discovery page

        `:return:` None

        `Created by:` Vasuja K
        """
        try:
            self.discovery_page.commonfun.open_url(url)
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
            status = self.discovery_page.commonfun.euro_login(params)
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
                self.discovery_page.commonfun.switch_page(**params)
            else:
                print("Please check that the input parameters have been provided",
                        self.switch_page.__doc__)
        except:
            raise AssertionError("Page Switch Failed!!")

    def select_show_and_return_title(self, **params):
        """
        `Description:` To select any show

        `:param` params: name of the show which need to be Selected

        `:return:` status

        `Created by:` Vasuja K
        """
        try:
            print("IN MAIN:")
            status = self.discovery_page.Disc_obj.select_show_and_return_title(params)
            return status
        except:
            raise AssertionError("Selecting the show Failed!!")

    def verify_favorites_status(self):
        """
        `Description:` To verify the Favorites status

        `:param` params: None

        `:return:` status

        `Created by:` Vasuja K
        """
        try:
            print("IN MAIN:")
            status = self.discovery_page.Disc_obj.verify_favorites_status()
            return status
        except:
            raise AssertionError("Verifying Favorites status Failed!!")

    def add_show_to_favorite_list(self, **params):
        """
        `Description:` To verify the Favorites status

        `:param` params: None

        `:return:` status

        `Created by:` Vasuja K
        """
        try:
            print("IN MAIN:")
            status = self.discovery_page.Disc_obj.add_show_to_favorite_list(params)
            return status
        except:
            raise AssertionError("Adding show to favorite list Failed!!")

    def verify_favorites_shows(self, **params):
        """
        `Description:` To verify favorites shows

        `:param` params: shows names

        `:return:` status

        `Created by:` Vasuja K
        """
        try:
            print("IN MAIN:")
            status = self.discovery_page.Disc_obj.verify_favorites_shows(params)
            return status
        except:
            raise AssertionError("Verifying the show Failed!!")

    def close_the_browser(self, **params):
        """
        `Description:` Close the browser object

        `:param` driver: WebDriver object

        `:return:` None

        `Created by:` Vasuja K
        """
        try:
            time.sleep(2)
            self.discovery_page.commonfun.close_browser()
        except:
            raise AssertionError("Close browser Failed!!")



