from selenium import webdriver
from selenium.webdriver import FirefoxProfile
import time

profile = FirefoxProfile('/home/syam.s/.mozilla/firefox/uzdp3719.FirefoxProfileTest')
cap=webdriver.DesiredCapabilities.FIREFOX.copy()
remote = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=cap,browser_profile=profile)

remote.get('https://www.eurosportplayer.com/')
time.sleep(20)

remote.quit()
