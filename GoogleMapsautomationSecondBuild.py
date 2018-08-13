from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def searchGoogleMaps(address, streetviewResponse):
    driver = webdriver.Firefox()
    driver.get('https://www.google.com/maps')

    element = driver.find_element_by_id('searchboxinput')
    element.send_keys(address, Keys.ENTER)
    if streetviewResponse.lower() == 'yes':
        sleep(5)
        class_name = 'section-image-pack-button'
        element = driver.find_element_by_name('Street View', Keys.ENTER)
    else:
        pass


street = input('Enter the address/location that you want to search!')
streetview = input('Do you want to go into street view?')
searchGoogleMaps(street, streetview)
