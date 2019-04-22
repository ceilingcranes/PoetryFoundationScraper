from bs4 import BeautifulSoup
import re
from selenium import webdriver
import pandas as pd
import requests
from time import sleep
import os
import pickle

def scrape_from_search(search_url):
    '''
    Given a search url, go through each subsequent page and scrape all poems from each url.
    :param search_url: string, search url from PoetryFoundation.org
    :return: list of urls for the poems
    '''

    url_pat = r'(.*page=)(\d+)(.*)'
    urlreg = re.match(url_pat, search_url)
    browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))

    pagenum = int(urlreg.group(2))
    poemurls = []
    atend = False
    while not atend:
        new_url = urlreg.group(1) + str(pagenum) + urlreg.group(3)

        browser.get(new_url)
        sleep(1)
        html = browser.page_source

        pagenum += 1
        soup = BeautifulSoup(html, 'html.parser')
        urlcontainer = soup.find('ol', {'class': 'c-vList c-vList_bordered c-vList_bordered_thorough'})
        if urlcontainer is not None:
            poems = urlcontainer.find_all('a', href=re.compile(r'\.*/poems/\d+/\.*'))

            for poem in poems:
                # print(poem.get('href'))
                poemurls.append(poem.get('href'))
        else:
            atend=True
        print(pagenum)
    return poemurls

def scrape_poem(poem_url):
    '''
    Get the poem text, author, and title from a url. Pulled from
    https://github.com/eli8527/poetryfoundation-scraper/blob/master/scrape.py
    :param poem_url: The url to an individual poem
    '''

    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    poemPage = requests.get(poem_url)
    poemSoup = BeautifulSoup(poemPage.text)

    poemTitle = poemSoup.find('h1')

    if poemTitle:

        poemContent = poemSoup.find('div', {'class': 'o-poem'})
        poemLines = poemContent.findAll('div')
        poemlines = ""
        print("=====================")
        for line in poemLines:
            print(line.text)
            poemlines = poemlines + line.text+'\n'
        print("=====================")
        print(poemlines)

if __name__=="__main__":

    # URL for free-verse poetry from poetryfoundation.org
    search_url = "https://www.poetryfoundation.org/poems/browse#page=1&sort_by=recently_added&forms=259"
    urls = scrape_from_search(search_url)

    # with open('poemurls','wb') as f:
    #     pickle.dump(urls, f)
    # with open('poemurls', 'rb') as f:
    #     urls = pickle.load(f)
    # print(len(urls))

    # test_poem = "https://www.poetryfoundation.org/poetrymagazine/poems/146236/cardi-b-tells-me-about-myself"
    # scrape_poem(test_poem)
