from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

def GotoWebsite(url):
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    element = driver.find_elements_by_tag_name('__w2_HOtqnFF_email')
    element.send_keys('test', Keys.ARROW_DOWN)
    # = requests.get(url)
    #content = r.text
    #soup = BeautifulSoup(content, 'html.parser')
    #print(soup.find_all('<input>'))

websiteName = input('Enter the website url that you want to go to')


if websiteName.startswith('https://') == False:
    print('Before' + websiteName)
    websiteName = 'https://www.' + websiteName
    print('After ' + websiteName)
    GotoWebsite(websiteName)
else:
    pass
