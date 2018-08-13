from bs4 import BeautifulSoup
import requests
import re


r = requests.get('https://www.jimsmowing.net')

content = r.text

soup = BeautifulSoup(content, 'html.parser')
#print(soup.find_all('p')[4].get_text())