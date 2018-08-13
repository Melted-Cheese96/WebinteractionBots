from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.google.com')

#elem = driver.find_element_by_name('q')
#elem.clear()
#elem.send_keys('Bing or google?')
#elem.send_keys(Keys.RETURN)
