import selenium
from selenium.webdriver.common.keys import Keys


def searchYoutube(vidName):
    driver = selenium.webdriver.Firefox()
    driver.get('https://www.youtube.com')
    element = driver.find_element_by_name('search_query')
    element.send_keys(vidName, Keys.ENTER)



videoName = input('Please type in your search query')
print('Searching youtube...')
searchYoutube(videoName)