from bs4 import BeautifulSoup
import requests


# Desc: Get the parsed BeautifulSoup structure,
#       parsed in html
# Param: URL to be parsed (string)
# Retval: Data structure of BeautifulSoup after parsed
def getBeautifulSoupInHtml(url):
    source = requests.get(url).text
    return BeautifulSoup(source, 'lxml')