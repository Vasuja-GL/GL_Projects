from selenium import webdriver
from selenium.webdriver import FirefoxProfile
profile = FirefoxProfile('/home/vasuja.kookkal/.mozilla/firefox/y3035bsl.default')
#browser = webdriver.Firefox(firefox_profile=profile)
driver = webdriver.Firefox(firefox_profile=profile,executable_path=r'/home/vasuja.kookkal/Desktop/GL_Projects/Eurosport_Automation/Selenium_Lib/ext_web_driver/linux/geckodriver')
driver.get('https://www.eurosportplayer.com/')