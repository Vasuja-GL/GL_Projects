"""
Description: WebElementAction module contains methods to perform action on web applications
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

#import custom_expected_conditions as CEC

import os
import inspect
import sys
import logging
#from log import log
import datetime


class WebElementAction:
    '''
    Methods to perform web operations are implemented in this class
    '''
    def __init__(self, browser):
        self._browser = browser

    def click_element(self, locator, replace_dict=None, value=None, index=None):
        """Click element identified by `locator`.

        """
        # if a locator returns more than 1 element and no value to match is supplied
        if index is not None and not value:
            self.elements = self._elements_finder(locator, replace_dict)
            if self.elements:
                self.elements[index].click()
                logging.error("Click operation successful for locator %s at index %s with no value to match" % (locator, str(index)))
                #log.mjLog.LogReporter("WebUIOperation", "debug", "Click operation successful for locator %s at index %s with no value to match" % (locator, str(index)))
                # returning as the element has already been clicked
                return
        # if a locator returns more than 1 element and some value to match is supplied
        if value:
            self.elements = self._elements_finder(locator, replace_dict)
            elements = [] # to store elements which has value(passed from param)
            if self.elements:
                for i in self.elements:
                    match_text = i.text.strip()
                    if "\n" in match_text:
                        match_text = map(str.strip, match_text.split("\n"))
                    if value in match_text:
                        elements.append(i)
                # if a locator returns more than 1 element and some value to match is supplied along with some index
                if index is not None:
                    elements[index].click()
                    logging.debug("Click operation successful for locator %s with value %s and index %s" % (locator, value, str(index)))
                    #log.mjLog.LogReporter("WebUIOperation", "debug", "Click operation successful for locator %s with value %s and index %s" % (locator, value, str(index)))
                else:
                    elements[0].click()
                    logging.debug("Click operation successful for locator %s with value %s and no index, so clicking the first occurrence" % (locator, value))
                    #log.mjLog.LogReporter("WebUIOperation", "debug", "Click operation successful for locator %s with value %s and no index, so clicking the first occurrence" % (locator, value))
        else:
            self.element = self._element_finder(locator, replace_dict)
            if self.element:
                self.element.click()
                logging.debug("Click operation successful- %s" % (locator))
                #log.mjLog.LogReporter("WebUIOperation", "debug", "Click operation successful- %s" % (locator))

    def input_text(self,locator, Text):
        """Types the given `text` into text field identified by `locator`.

        """
        self.element = self._element_finder(locator)
        if self.element:
            self.element.clear()
            self.element.send_keys(Text)
            logging.debug("Input_text operation successful- %s" %(locator))
            #log.mjLog.LogReporter("WebUIOperation","debug","Input_text operation successful- %s" %(locator))

    def explicit_wait(self, element, waittime=20, replace_dict=None, ec='visibility_of_element_located', msg=None, msg_to_verify=None, condition_category="until"):
        """
        explicit_wait() is used to wait until element is displayed & enabled
        """
        if element[0:2] == "//":
            self.elementAttr = {
                "ELEMENT_TYPE": "unused placeholder",
                "BY_TYPE": "xpath",
                "BY_VALUE": element
            }
        else:
            self.elementAttr = self._browser._locator_converter(element, replace_dict)

        if 'not' in condition_category:
            wait = WebDriverWait(self._browser.get_current_browser(), waittime).until_not
            error_msg = "The element <%s> can not be located after explicit wait." % element
        else:
            wait = WebDriverWait(self._browser.get_current_browser(), waittime).until
            error_msg = "Could not locate element <%s> during explicit wait." % element
        result = None
        try:
            condition = getattr(EC, ec)
        except AttributeError as e:
            logging.error(e)
            #condition = getattr(CEC, ec)
        locator = getattr(By, self.elementAttr['BY_TYPE'].upper())
        try:
            if msg:
                result = wait(condition(msg))
            elif msg is None and msg_to_verify is None:
                result = wait(condition((locator, self.elementAttr["BY_VALUE"])))
            elif msg_to_verify:
                result = wait(condition((locator, self.elementAttr["BY_VALUE"]), msg_to_verify))
        except Exception as e:
            raise Exception(error_msg + str(e))

        return result
    
    def mouse_hover(self, locator):
        '''Mouse hover on element identified by `locator`.

        Key attributes for arbitrary elements are `id` and `name`
        '''
        self.element = self._element_finder(locator)
        if self.element:
            ActionChains(self._browser.get_current_browser()).move_to_element(self.element).perform()
            logging.debug("mouse_hover operation successful- %s" %(locator))
            #log.mjLog.LogReporter("WebUIOperation","debug","mouse_hover operation successful- %s" %(locator))

    def maximize_browser_window(self):
        """Maximizes the currently opened browser window
        """
        self._current_browser().maximize_window()
        logging.debug("maximize_browser_window - operation successfull")
        #log.mjLog.LogReporter("WebUIOperation","debug","maximize_browser_window - operation successfull")

    def takeScreenshot(self, funcName, location=None):
        """
        Method to save screen shot to a given path with the function name
        :return: None
        """
        # trying to figure out the report location
        if location is None:
            for frame in inspect.stack():
                if "page" in frame[1] and "Component" in frame[1]:
                    feature_file = frame[1]
                    location = feature_file.split("page")[0]
                    break
                elif "lib" in frame[1] and "Component" in frame[1]:
                    feature_file = frame[1]
                    location = feature_file.split("lib")[0]
                    break
            else:
                location = os.path.dirname(os.path.dirname(__file__))
        path = location+"\\reports\\report_"+str(datetime.datetime.now().date())+os.sep
        try:
            if not os.path.exists(path):
                print("Report path not found.Creating...")
                os.makedirs(path)
            name = path+funcName+str(datetime.datetime.now().time()).replace(":","_")+".png"
            print(name)
            self._browser.get_screenshot_as_file(name)
        except Exception as e:
            print(e)


# Private method
    def _element_finder(self, locator, replace_dict=None):
        '''
        _element_finder() - Method to invoke element_finder from browser class
        '''
        return self._browser.element_finder(locator, replace_dict)

    def _elements_finder(self, locator, replace_dict=None):
        '''
        _elements_finder() - Method to invoke elements_finder from browser class
        '''
        return self._browser.elements_finder(locator, replace_dict)
