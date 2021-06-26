##  Run scrapy to pull quote
#   Developer: nickumia

global IMG

import json
import os

IMG = True

def get_quote():
    if not IMG:
        os.system("sed -i 's/https:\/\/www.insightoftheday.com/https:\/\/quotes.toscrape.com/' /app/gather_quotes/spiders/quotes_spider.py")
    else:
        os.system("sed -i 's/https:\/\/quotes.toscrape.com/https:\/\/www.insightoftheday.com/' /app/gather_quotes/spiders/quotes_spider.py")
    os.system("rm -rf quotes.json")
    os.system("scrapy crawl quotes -o quotes.json")
    quotes = json.load(open("quotes.json"))
    for quote in quotes:
        return quote
