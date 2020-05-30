from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


# Desc: Get the parsed BeautifulSoup structure,
#       parsed in html
# Param: URL to be parsed (string)
# Retval: Data structure of BeautifulSoup after parsed
def getBeautifulSoupInHtml(url):
    site = url
    # References: https://stackoverflow.com/a/13055444
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    return BeautifulSoup(page, 'html')