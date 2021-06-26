##  Query links for the quotes
#   Developer: nickumia


import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/',
        'https://www.insightoftheday.com/'
    ]

    def parse(self, response):
        # Text
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        # Img

