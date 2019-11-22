from selenium import webdriver
from time import sleep

fp=None
fp = webdriver.FirefoxProfile()
fp.set_preference("plugin.state.java", 2)
cap=webdriver.DesiredCapabilities.FIREFOX.copy()
remote = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=cap)

remote.get('https://www.eurosportplayer.com/')
sleep(10)

remote.quit() 
