from bs4 import BeautifulSoup
import requests
import re
import sys 




def writetoDoc(docname, data, urlname):
    document = open(docname, 'w+')
    document.write(str(data))
    document.close()

def Crawlweb(url, tags):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    data1 = {}
    website = requests.get(url, headers=headers, data=data1)
    content = website.text

    soup = BeautifulSoup(content, 'html.parser')
    final = soup.find_all(tags)
    print(final)
    write = input('Do you want to write parsed data to a file?')
    if write.lower() == 'yes':
        name = input('Enter name for new file')
        writetoDoc(name, final, url)
        print('Data has been written to file')
        sleep(1)
        print('Quitting...')
        sys.exit()
    else:
        print('Closing program....')
        sys.exit()


url = input('Enter the url of the website that you want data from')
if url.startswith('https://') == False:
    url = 'https://www.' + url
    print(url)
else:
    pass
tag = input('What tag do you want info from?')
Crawlweb(url, tag)
