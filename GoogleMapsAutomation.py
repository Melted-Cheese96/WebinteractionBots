from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def searchGoogleMaps(address):
    driver = webdriver.Firefox()
    driver.get('https://www.google.com/maps')

    element = driver.find_element_by_id('searchboxinput')
    element.send_keys(address, Keys.ENTER)

street = input('Enter the address/location that you want to search!')
searchGoogleMaps(street)
