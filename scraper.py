from bs4 import BeautifulSoup
import urllib.request as urllib2
import re
from html.parser import HTMLParser
import pandas as pd
import requests

def scrape_from_search(search_url, df):
    '''
    Given a search url, go through each subsequent page and scrape all poems from each url.
    :param search_url: string, search url from PoetryFoundation.org
    :return: pandas dataframe containing title, author, and poem text in each row
    '''
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    url_pat = r'(.*page=)(\d+)(.*)'
    urlreg = re.match(url_pat, search_url)
    print(urlreg.group(1))
    print(urlreg.group(2))

    pagenum = int(urlreg.group(2))
    # TODO: Update to automatically break
    while pagenum < 253:
        new_url = urlreg.group(1) + str(pagenum) + urlreg.group(3)
        print(new_url)
        # page = urllib2.urlopen(new_url)
        page = requests.get(new_url, headers=headers)
        pagenum += 1
        soup = BeautifulSoup(page.text)
        urllist = soup.find('ol', {'class': 'c-vList c-vList_bordered c-vList_bordered_thorough'})
        


def scrape_poem(poem_url):
    '''
    Get the poem text, author, and title from a url.
    :param poem_url:
    :return:
    '''


if __name__=="__main__":

    # URL for free-verse poetry from poetryfoundation.org
    search_url = "https://www.poetryfoundation.org/poems/browse#page=1&sort_by=recently_added&forms=259"
    scrape_from_search(search_url, None)

