##  Query links for the quotes
#   Developer: nickumia

    
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.insightoftheday.com/'
    ]

    def parse(self, response):
        try:
            # Img
            for quote in response.css('div.daily-post'):
                return {
                    'title': quote.css('h2.entry-title::text').get(),
                    'text': None,
                    'img': quote.css('div.quote a p img::attr(src)').extract()
                }
        except BaseException:
            pass
