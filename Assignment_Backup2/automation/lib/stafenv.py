
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "page"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Selenium_Lib"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Selenium_Lib",
                             "utils"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Selenium_Lib",
                             "web_wrappers"))
if 'PYTHONPATH' not in os.environ:
    os.environ['PYTHONPATH'] = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Selenium_Lib")

print(sys.path)