"""
Module: Browser
File name: Browser.py
Description: Browser module contains methods to control & retrieve information from web Browsers
"""
# Selenium Modules
from robot.api.logger import console, info

# Python Modules
import copy
import sys
import os

from log import log

sys.path.append(os.path.join(os.path.dirname((os.path.dirname(os.path.dirname(__file__)))), "utils"))
from mapMgr import mapMgr

from selenium.common.exceptions import (
    NoSuchAttributeException,
    NoSuchElementException,
    NoSuchFrameException,
    NoSuchWindowException,
    StaleElementReferenceException,
    WebDriverException,
)


class Browser:
    """
        Base class for Web Automation uses python selenium Web Driver for this module
    """
    _DEFAULT_TIMEOUT = 15
    elem_locators = {
        "id": "find_elements_by_id",
        "accessibility": "find_element_by_accessibility_id",
        "name": "find_elements_by_name",
        "xpath": "find_elements_by_xpath",
        "tag": "find_elements_by_tag_name",
        "css_class": "find_elements_by_class_name",
        "text": "find_element_by_link_text",
        "css_selector": "find_elements_by_css_selector"
    }

    def __init__(self, params):
        self.elements = {
            "id": self._browser.find_elements_by_id,
            "name": self._browser.find_elements_by_name,
            "xpath": self._browser.find_elements_by_xpath,
            "tag": self._browser.find_elements_by_tag_name,
            "css_class": self._browser.find_elements_by_class_name,
            "text": self._browser.find_element_by_link_text,
            "css_selector": self._browser.find_elements_by_css_selector
        }
        self._browser.implicitly_wait(10)

    def get_current_browser(self):
        return self._browser

    def get_locator(self, by):
        '''
        get_locator() will return element identifier object e.g. find_elements_by_id
        '''
        if by is None:
            log.mjLog.LogReporter("Browser", "error", "Attribute to identify element is empty")
            return None

        return self.elements[by.lower()]

    # def go_to(self, url,browser):
    #     '''
    #         go_to() method goes to the specific URL after the browser instance launches
    #     '''
    #     browser.get(url)

    def get_screenshot_as_file(self, screenshot_file):
        '''
            get_screenshot_as_file() - Gets the screenshot of the current window.
            Returns False if there is any IOError, else returns True.
        '''
        self._browser.get_screenshot_as_file(screenshot_file)

    def get_elements(self, By=None, ByValue=None, index=None):
        '''
            get_elements() api works for multiple web elements Identification
            on web pages
        '''
        try:
            self.By = By
            self.ByValue = ByValue
            if self.By is None or self.ByValue is None:
                log.mjLog.LogReporter("Browser", "error", "Element by and Element attribute value is empty")
                return None

            # Getting element identifier object
            self.elementObj = self.get_locator(self.By.lower())

            # Returning identified element
            self.elementObjList = self.elementObj(self.ByValue)
            if index is None:
                return self.elementObjList
            else:
                if index >= len(self.elementObjList):
                    log.mjLog.LogReporter("Browser", "error", "Element index is outside of number of elements found")
                    return None
                else:
                    if (not self.elementObjList[index].is_displayed()) or (not self.elementObjList[index].is_enabled()):
                        log.mjLog.LogReporter("Browser", "error", "The element is found but is not enabled/visible.")
                        return None

                    return [self.elementObjList[index]]

        except (WebDriverException, NoSuchElementException) as e:
            log.mjLog.LogReporter("Browser", "error", "Browser.get_elements: Exception: %s" % str(e))

    def get_element(self, By=None, ByValue=None, index=None):
        '''
            get_element() api works for web element Identification
            on web pages uses get_elements() method and returns single
            element on call
        '''
        try:
            log.mjLog.LogReporter("Browser", "debug", "Browser.get_elements: By=%s, ByValue=%s" % (By, ByValue))
            if index is not None:
                self.elementRef = self.get_elements(By, ByValue, index)
            else:
                self.elementRef = self.get_elements(By, ByValue)

            if len(self.elementRef) == 0:
                raise Exception("0 elements found.")
            elif len(self.elementRef) > 1:
                log.mjLog.LogReporter("Browser", "warning",
                                      ">1 Elements found using : By=%s, ByValue=%s" % (By, ByValue))
                raise AssertionError(">1 element found")

            else:
                log.mjLog.LogReporter("Browser", "debug", "Element identified: By=%s, ByValue=%s" % (By, ByValue))
                return self.elementRef[0]
        except (WebDriverException, NoSuchElementException) as e:
            import traceback
            raise AssertionError("Exception occured in element identification. Traceback: %s" % traceback.format_exc())

    def quit(self):
        '''
            Close the Browser
        '''
        try:
            self._browser.quit()
        except:
            import time
            time.sleep(2)
            try:
                self._browser.quit()
            except:
                log.mjLog.LogReporter("Browser", "error", "Webdriver was not able to close browser.")
                import traceback
                log.mjLog.LogReporter("Browser", "debug", " %s" % traceback.format_exc())

    def close(self):
        '''
        Close the current browser window
        '''
        try:
            self._browser.close()
        except:
            log.mjLog.LogReporter("Browser", "error", "Webdriver is not able to close corrent browser.")
            import traceback
            log.mjLog.LogReporter("Browser", "debug", " %s" % traceback.format_exc())

    def close_browser(self):
        '''
        Close the current browser window
        '''
        try:
            self._browser.close()
        except:
            import traceback
            log.mjLog.LogReporter("Browser", "error",
                                  "Error in closing current browser: " + str(traceback.format_exc()))

    def _map_converter(self, locator, replace_dict=None):
        '''
        map_converter() - Gets element attributes from map files
        Return dictionary
        '''
        self.elementAttr = copy.deepcopy(mapMgr.__getitem__(locator))
        if replace_dict:
            for key in replace_dict:
                xpath = self.elementAttr['BY_VALUE']
                r = '!'+key+'!'
                self.elementAttr['BY_VALUE'] = xpath.replace(r, str(replace_dict[key]))

        info(self.elementAttr)
        return self.elementAttr

    def element_finder(self, locator, replace_dict=None):
        '''
        element_finder() - locates the element in the web application
        return element object
        '''
        try:
            if locator[0:2] == "//":
                self.elementAttr = {
                    "ELEMENT_TYPE": "unused placeholder",
                    "BY_TYPE": "xpath",
                    "BY_VALUE": locator
                }
            else:
                self.elementAttr = self._map_converter(locator, replace_dict)

            if self.elementAttr:
                if len(self.elementAttr.keys()) == 3:
                    self.element = self.get_element(By=self.elementAttr["BY_TYPE"],
                                                    ByValue=self.elementAttr["BY_VALUE"])
                elif len(self.elementAttr.keys()) == 4:
                    self.element = self.get_element(By=self.elementAttr["BY_TYPE"],
                                                    ByValue=self.elementAttr["BY_VALUE"],
                                                    index=self.elementAttr["INDEX"])
                else:
                    log.mjLog.LogReporter("WebUIOperation", "error",
                                          "Element property in map file are not proper  - %s" % (locator))
                    raise AssertionError("Element property in map file are not proper  - %s" % (locator))
                return self.element
            else:
                raise Exception("No element returned for provided locator <%s>"%locator)
        except:
            log.mjLog.LogReporter("Browser", "error",
                                  "element_finder - No or more than 1 element returned for provided locator" + str(sys.exc_info()))
            raise AssertionError("Browser- element_finder - No or more than 1 element returned for provided locator")

    def elements_finder(self, locator, replace_dict=None):
        '''
        elements_finder() - locates multiple elements in the web application
        return element object
        '''

        try:
            if locator[0:2] == "//":
                self.elementAttr = {
                    "ELEMENT_TYPE": "unused placeholder",
                    "BY_TYPE": "xpath",
                    "BY_VALUE": locator
                }
            else:
                self.elementAttr = self._map_converter(locator, replace_dict)

            if self.elementAttr:
                if len(self.elementAttr.keys()) == 3:
                    self.elementlist = self.get_elements(By=self.elementAttr["BY_TYPE"],
                                                         ByValue=self.elementAttr["BY_VALUE"])
                elif len(self.elementAttr.keys()) == 4:
                    self.elementlist = self.get_elements(By=self.elementAttr["BY_TYPE"],
                                                         ByValue=self.elementAttr["BY_VALUE"],
                                                         index=self.elementAttr["INDEX"])
                else:
                    log.mjLog.LogReporter("WebUIOperation", "error",
                                          "Element property in map file are not proper  - %s" % (locator))
                    raise AssertionError("Element property in map file are not proper  - %s" % (locator))
                return self.elementlist
            else:
                raise Exception("No element returned for provided locator <%s>" % locator)
        except:
            log.mjLog.LogReporter("Browser", "error",
                                  "elements_finder - No element returned for provided locator" + str(sys.exc_info()))
            raise AssertionError("Browser- elements_finder - No element returned for provided locator")
