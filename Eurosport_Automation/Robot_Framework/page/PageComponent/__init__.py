from On_Demand import On_Demand
from Euro_CommonFunctionality import Euro_CommonFunctionality


class EuroPage(object):
    """Module for all the Eurosports pages"""

    def __init__(self, browser):
        self.on_demand = On_Demand(browser)
        self.common_fun = Euro_CommonFunctionality(browser)
