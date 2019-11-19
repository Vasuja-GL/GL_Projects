"""
 Custom Expected Wait Conditions which are generally useful within web driver tests.
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException




class length_of_drop_down_is(object):

    def __init__(self, locator, value):
        self.locator = locator
        self.value = value

    def __call__(self, driver):
        element = _find_element(driver, self.locator)
        length = len(element.find_elements_by_tag_name('option'))
        print("length is %d" %length)
        if length > self.value:
            return element
        else:
            return False

    def _find_element(driver, by):
        """Looks up an element. Logs and re-raises ``WebDriverException``
        if thrown."""
        try:
            return driver.find_element(*by)
        except NoSuchElementException as e:
            raise e
        except WebDriverException as e:
            raise e


    def _find_elements(driver, by):
        try:
            return driver.find_elements(*by)
        except WebDriverException as e:
            raise e
