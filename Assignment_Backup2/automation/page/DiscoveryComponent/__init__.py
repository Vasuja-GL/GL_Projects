from Discovery_page import Discovery_page
from Disc_CommonFunctionality import Disc_CommonFunctionality


class DiscoveryPage(object):
    """Module for all the Discovery pages"""

    def __init__(self, browser):
        self.Disc_obj = Discovery_page(browser)
        self.commonfun = Disc_CommonFunctionality(browser)
