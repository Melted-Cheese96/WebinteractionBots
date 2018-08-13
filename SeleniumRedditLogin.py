from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.quora.com')

element = driver.find_element_by_id('password')
element = driver.find_element_by_name('password')
