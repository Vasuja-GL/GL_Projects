"""
This is an updated Browser class that inherits the remote driver version of Browser

"""
import os
import sys

import logging
import tempfile


from log import log

from selenium import webdriver
from robot.api import logger
from Browser import Browser

class LocalBrowser(Browser):
    _DEFAULT_TIMEOUT = 15
    _BROWSER_INFO_WIN = {
                     'chrome'        : {'webdriver_path': os.path.join(
                                            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                            'ext_web_driver','windows', 'chromedriver.exe')},
                     }
    _BROWSER_INFO_LINUX = {'firefox': {'webdriver_path': os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'ext_web_driver', 'linux', 'geckodriver.exe')},
        'ie': {'webdriver_path': '..\\ext_web_driver\\linux\\IEDriverServer'},
        'edge': {'webdriver_path': '..\\ext_web_driver\\linux\\MicrosoftWebDriver'},
        'local_chrome': {
            'webdriver_path': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ext_web_driver', 'linux',
                                           'chromedriver')},
        'chrome': {'webdriver_path': os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'ext_web_driver', 'linux', 'chromedriver')},
        'ghost': {'webdriver_path': '..\\ext_web_driver\\linux\\phantomjs'}}

    def __init__(self, browser="chrome", crx=None, notifications=None):

        selenium_logger = logging.getLogger("selenium.webdriver.remote.remote_connection")
        selenium_logger.setLevel(logging.WARNING)
        self.console_log = tempfile.NamedTemporaryFile(delete=False, suffix=".log")

        # initializing based on platform
        if sys.platform == "win32":
            self._BROWSER_INFO = self._BROWSER_INFO_WIN
            self.user_data_dir = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data"
        elif sys.platform == "linux2":
            self._BROWSER_INFO = self._BROWSER_INFO_LINUX
            self._FIREFOX_DEFAULT_PATH = "//Applications//Firefox.app//Contents//MacOS//firefox-bin"
            self.user_data_dir = "//Users//administrator//Library//Application Support//Google//Chrome"

        self.browsertype = browser
        if self.browsertype in self._BROWSER_INFO.keys():
            self._browser = self.create_webdriver(self.browsertype,crx, notifications)
        else:
            raise Exception("\nBrowser not supported. Supported browsers: %s\n" %
                            self._BROWSER_INFO.keys())

        self.elements = {
            "id"            : self._browser.find_elements_by_id,
            "name"          : self._browser.find_elements_by_name,
            "xpath"         : self._browser.find_elements_by_xpath,
            "tag"           : self._browser.find_elements_by_tag_name,
            "css_class"     : self._browser.find_elements_by_class_name,
            "text"          : self._browser.find_element_by_link_text,
            "css_selector"  : self._browser.find_elements_by_css_selector
        }
        log.setLogHandlers()

    # def create_webdriver(self, browser="chrome", crx=None, notifications=None):
    #     """
    #     Create the webdriver object depending on the browser type
    #             Args:
    #                 browser - type of browser. Supported options: chrome, firefox, ie, headless, edge
    #             Returns:
    #                 Webdriver(object) depending on the type of the browser
    #     """
    #
    #     if browser == 'chrome' and sys.platform == "linux2":
    #         options = webdriver.ChromeOptions()
    #
    #         #options.add_argument(r"--no-sandbox")
    #        # options.add_argument('--profile-directory=Test')
    #         options.add_argument("--user-data-dir=/home/vasuja.kookkal/.cache/google-chrome/Default/Cache")
    #         options.add_argument("--profile-directory=Default")
    #         # options.add_argument('--user-data-dir=/home/vasuja.kookkal/.config/google-chrome/Profile 1')
    #         # options.add_argument('--args --profile-directory="Profile 1"')
    #         testdriver = webdriver.Chrome(self._BROWSER_INFO[browser]['webdriver_path'], chrome_options=options)
    #
    #     else:
    #         options = webdriver.ChromeOptions()
    #         if crx:
    #             logger.warn("Using crx app '%s'" % crx)
    #             options.add_extension(crx)
    #
    #         if notifications:
    #             if notifications == "allow":
    #                 notif_index = 1
    #             else:
    #                 pass
    #                 # notif_index = 2
    #             prefs = {"profile.default_content_setting_values.notifications": notif_index}
    #         else:
    #             pass
    #             # prefs = {"profile.default_content_setting_values.notifications": 2}
    #         options.add_experimental_option("prefs", prefs)
    #
    #         service_args = []
    #         if self.console_log:
    #             service_args.append("--verbose")
    #             service_args.append("--log-path=" + self.console_log.name)
    #
    #         testdriver = webdriver.Chrome(self._BROWSER_INFO[browser]['webdriver_path'],
    #                                       service_args=service_args,
    #                                       chrome_options=options)
    #     testdriver.implicitly_wait(self._DEFAULT_TIMEOUT)
    #     return testdriver

    def create_webdriver(self, browser="chrome", crx=None, notifications=None):
        """
        Create the webdriver object depending on the browser type
                Args:
                    browser - type of browser. Supported options: chrome, firefox, ie, headless, edge
                Returns:
                    Webdriver(object) depending on the type of the browser
        """

        if browser == 'chrome' and sys.platform == "linux2":
            options = webdriver.ChromeOptions()
            options.add_argument(r"--no-sandbox")
            testdriver = webdriver.Chrome(self._BROWSER_INFO[browser]['webdriver_path'], chrome_options=options)

        else:
            options = webdriver.ChromeOptions()
            if crx:
                logger.warn("Using crx app '%s'" % crx)
                options.add_extension(crx)

            if notifications:
                if notifications == "allow":
                    notif_index = 1
                else:
                    notif_index = 2
                prefs = {"profile.default_content_setting_values.notifications": notif_index}
            else:
                prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)

            service_args = []
            if self.console_log:
                service_args.append("--verbose")
                service_args.append("--log-path=" + self.console_log.name)

            testdriver = webdriver.Chrome(self._BROWSER_INFO[browser]['webdriver_path'],
                                          service_args=service_args,
                                          chrome_options=options)
        testdriver.implicitly_wait(self._DEFAULT_TIMEOUT)
        return testdriver

