
import re
import os
import sys

#from log import log


class mapParser:
    """ mapParser class is used to read and write configuration files. """

    def __init__(self, filename=None, rtool=None):
        self.map_dict = {}
        self.map_key_list = []
        self.rtool = rtool
        if not filename:
            logging.error("__init__ - File name not mentioned")
            #log.mjLog.LogReporter("map_parser", "error", "__init__ - File name not mentioned")

        try:
            fileobj = open(filename, "r")
            other_value_line_count = 0
            for line in fileobj:
                # ignoring blank lines and the comments(starting with #)
                if not line.startswith("#") and not line.isspace():
                    if '==' in line and line.count('#') >= 2:
                        eleList = line.split('==')
                        if len(eleList) >= 2:
                            # Remove \n and leading and trailing spaces from value and then save
                            value_parts = [ele.strip() for ele in eleList[1].split('#')]
                            key = eleList[0].strip()
                            if key not in self.map_key_list:
                                self.map_key_list.append(key)
                                # if condition is to distinguish between locator for web-element and desktop elements
                                if (key.endswith("_win")) or (key.endswith("_mac")):
                                    self.map_dict[key] = {
                                        "ELEMENT_TYPE": value_parts[0],
                                        "APP_NAME": value_parts[1],
                                        "IDENTIFIERS": value_parts[2]
                                    }
                                else:
                                    self.map_dict[key] = {
                                        "ELEMENT_TYPE": value_parts[0],
                                        "BY_TYPE": value_parts[1],
                                        "BY_VALUE": value_parts[2]
                                    }
                            else:
                                logging.error("duplicate found at line %s in file %s" % (line, filename))
                                #log.mjLog.LogReporter("map_parser", "error",
                                                     # "duplicate found at line %s in file %s" % (line, filename))
                    else:
                        logging.error("__init__ - Xpath %s in file %s does not contain == or it contain only 1 #" % (line, filename))
                        #log.mjLog.LogReporter("map_parser", "error",
                                            #  "__init__ - Xpath %s in file %s does not contain == or it contain only 1 #" % (line, filename))


                    if len(value_parts) > 3:
                        self.map_dict[key]["INDEX"] = int(value_parts[3])
                    elif len(value_parts) > 4:
                        key = 'other_value_line_count_' + str(other_value_line_count)
                        other_value_line_count = other_value_line_count + 1
                        self.map_dict[key] = line
                        self.map_key_list.append(key)
            fileobj.close()
        except:
            logging.error("__init__ - Error: " + str(sys.exc_info()))
            #log.mjLog.LogReporter("map_parser", "error", "__init__ - Error: " + str(sys.exc_info()))
            raise Exception

    def __str__(self):
        ret_str = ""
        for key in self.map_key_list:
            value = self.map_dict[key]
            #        print " * * * * kay=", key, " value =",  value
            if re.search("other_value_line_count", key):
                ret_str = ret_str + str(value)
            else:
                ret_str = ret_str + str(key) + '=' + str(value) + '\n'
        # print ret_str
        return ret_str

    def __getitem__(self, key):
        if key in list(self.map_dict.keys()):
            return self.map_dict[key]
        else:
            return None

    def __setitem__(self, key, value):
        self.map_dict[key] = str(value).strip()
        if not key in self.map_key_list: self.map_key_list.append(key)

    def remove(self, key):
        value = None
        if key in self.config.key_list:
            value = self.map_dict[key]
            self.map_key_list.remove(key)
            del self.map_dict[key]

    def update_dictionary(self, param_dict):
        for key in param_dict.keys():
            self.map_dict[key] = param_dict[key]

    def write(self, fileobj):
        fileobj.write(str(self))


