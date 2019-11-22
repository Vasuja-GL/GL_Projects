import selenium
import time
from selenium import webdriver


#driver =webdriver.Chrome('/usr/local/bin/chromedriver')

options = webdriver.ChromeOptions()

            #options.add_argument(r"--no-sandbox")
           # options.add_argument('--profile-directory=Test')
options.add_argument("--user-data-dir='/home/syam.s/.cache/google-chrome/Default/Cache'")
options.add_argument("--profile-directory='Default'")
#options.add_argument("--user-data-dir=/home/syam.s/.config/google-chrome/'Profile 1'")
#options.add_argument("--profile-directory='Profile 1'")
driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
driver.execute_script("window.open('https://eurosportplayer.com');")
time.sleep(10)
driver.quit()
