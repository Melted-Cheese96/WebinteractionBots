import requests

url = 'https://www.google.com.au'

data = {'title': 'test', 'description': 'yes'}
r = requests.post(url, data=data)
print(r)
