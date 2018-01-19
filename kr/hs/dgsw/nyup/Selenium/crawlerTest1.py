from selenium import webdriver

driver = webdriver.Chrome('../Driver/chromedriver')
driver.implicitly_wait(3)
driver.get('https://google.com')
