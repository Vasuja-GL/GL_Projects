"""
locator files manager class
"""
import os
from locator_parser import locatorParser


class locatorMgr:
    '''
        locatorMgr parsers all the locator files inside locator directory and converts them into dictionary
    '''
    objRepository = {}
    objRepoList = []
    @staticmethod
    def create_locatorlist(component = "Eurosports"):
        try:
            # Listing all the file in the locator directory
            # creating the locator directory path
            locatordirectory = None
            filelist = []
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            if "Eurosports".lower() in component.lower():
                locatordirectory = os.path.join(base_path, "Robot_Framework", "locator", component)
            else:
                raise Exception("Component %s is not supported!" % component)
                
            if isinstance(component, str):
                if os.path.isdir(locatordirectory):
                    print("Locator directory for <%s> is <%s>"%(component, locatordirectory))
                else:
                    raise AssertionError("<%s> Directory not found for <%s>" %(locatordirectory, component))

            for dirname, dirnames, filenames in os.walk(locatordirectory):
                filelist.extend([os.path.join(dirname, filename) for filename in filenames])
                 
            for file in filelist:
                # Parsing all the locator file one by one and updating objRepository dictionary
                map_obj = locatorParser(file)
                locatorMgr.objRepository.update(map_obj.map_dict)
                locatorMgr.objRepoList.append(map_obj.map_key_list)
        except:
            return False
        
    # Method to get objList
    @staticmethod
    def getMapKeyList():
        return locatorMgr.objRepoList

    # Method to get objDictionary
    @staticmethod
    def getMapDict():        
        return locatorMgr.objRepository

    # Method to get element from objRepository
    @staticmethod
    def __getitem__(key):
        if key in list(locatorMgr.objRepository.keys()):
            return locatorMgr.objRepository[key]
        else:
            return None

