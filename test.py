from selenium import webdriver
from selenium.webdriver import FirefoxProfile
import time

profile = FirefoxProfile('/home/syam.s/.mozilla/firefox/t59w63h4.default')
desiredCapabilities={
"browserName":"firefox"
}

remote = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=desiredCapabilities,browser_profile=profile)

remote.get('https://www.eurosportplayer.com/')
time.sleep(20)

remote.quit()
