# -*- coding: utf-8 -*-

## Base URL is https://www.marketwatch.com/investing/stock/

import requests
from bs4 import BeautifulSoup

tickers = ["tsla", "bngo", "rr", 'jagx', 'gme']

lookupDict = {} ## The main dictionary

for ticker in tickers:
    page = requests.get('https://www.marketwatch.com/investing/stock/' + ticker)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    result = soup.find('h3', class_ = 'intraday__price')
    
    price = result.text.strip().split('\n')
    price[1] = float(price[1])

    lookupDict[ticker] = price
    
print (lookupDict)