##  Query links for the quotes
#   Developer: nickumia

    
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/',
    ]

    def parse(self, response):

        try:
            # Text
            for quote in response.css('div.quote'):
                if quote.css('span.text::text').get() != None:
                    return {
                        'text': quote.css('span.text::text').get(),
                        'author': quote.css('small.author::text').get(),
                        # 'tags': quote.css('div.tags a.tag::text').getall(),
                        'img': None
                    }
        except BaseException:
            pass

        try:
            # Img
            for quote in response.css('div.daily-post'):
                return {
                    'text': quote.css('h2.entry-title::text').get(),
                    'img': quote.css('div.quote a p img::attr(src)').extract()
                }
        except BaseException:
            pass
