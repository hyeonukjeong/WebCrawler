from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../Driver/chromedriver')
driver.implicitly_wait(3)
driver.get('https://accounts.google.com/signin/v2/identifier?uilel=3&service=youtube&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%26hl%3Den%26action_handle_signin%3Dtrue%26app%3Ddesktop&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.find_element_by_name('identifier').send_keys('hujeong1004@gmail.com')
driver.find_element_by_xpath("/html[@class='CMgTXc']/body[@id='yDmH0d']/div[@class='uc81Ff wKBl8c']/div[@id='initialView']/div[@class='bdf4dc']/div[@id='view_container']/form[@class='RFjuSb bxPAYd k6Zj8d']/div[@class='hMxfuf']/div/div[@class='FgbZLd r5i3od']/div[2]/div[@class='mUbCce fKz7Od YYBxpf KEavsb M9Bg4d']/content[@class='xjKiLb']/span/span/svg[@class='[object SVGAnimatedString]']").click()
