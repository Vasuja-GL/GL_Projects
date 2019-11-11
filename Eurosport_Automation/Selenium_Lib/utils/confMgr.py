###############################################################################
## Module: confMgr
## File name: confMgr.py
## Description: configuration manager to associate stream & Rotating file handlers
###############################################################################
import os

CONFIG_FILE_NAME = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/STAF.conf")
#CONFIG_FILE_NAME = '../config/STAF.conf'

#-------------
from config_parser import ConfigParser
class confMgr(object):
    feature_conf = ConfigParser(CONFIG_FILE_NAME)

    @classmethod
    def getConfigKeyList(self):
        return confMgr.feature_conf.config_key_list

    @classmethod
    def getConfigMap(self):
        return confMgr.feature_conf.config_map

    @classmethod
    def setConfigMap(self, new_dict):
        confMgr.feature_conf.update_dictionary(new_dict)
