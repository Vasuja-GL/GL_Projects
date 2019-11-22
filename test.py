from selenium import webdriver

desiredCapabilities={
"browserName":"chrome"
}

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities = desiredCapabilities);
driver.get("https://www.google.co.in/");
print driver.title;
driver.quit();
