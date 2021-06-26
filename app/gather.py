##  Run scrapy to pull quote
#   Developer: nickumia


import json
import os


def get_quote():
    os.system("rm -rf quotes.json")
    os.system("scrapy crawl quotes -o quotes.json")
    quotes = json.load(open("quotes.json"))
    for quote in quotes:
        if quote['text'] != None:
            return quote
