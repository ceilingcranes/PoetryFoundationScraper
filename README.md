# Poetry Foundation Scraper
A webscraper that pulls from the Poetry foundation search page to find the URLs of all poems that match with the search criteria and downloads them all as part of a Pandas dataframe. 

## Requirements
1. BeautifulSoup
2. Pandas
3. Selenium - must have the [Selenium](https://www.seleniumhq.org/) package installed, and include the Chrome browser driver. To do this, go [download the Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches the version of Chrome you're using and place the driver either in the same directory as scraper.py or on the PATH.
If you want to use a different browser, change the line `browser = webdriver.Chrome()` to match whatever browser you're using. More information can be found in the [Selenium docs.](https://seleniumhq.github.io/selenium/docs/api/py/api.html)

To run, first get all URLs using the `scrape_from_search` method, which returns a list of URLs. Individual URLs can be passed into the method `scrape_poem()` to get the information on the poem, including the author, title, and poem text. The code for individual poem scraping is based on code from the [poetryfoundation-scraper repository.](https://github.com/eli8527/poetryfoundation-scraper/blob/master/scrape.py)
