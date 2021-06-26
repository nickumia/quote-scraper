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
                        'title': ", ".join(quote.css('div.tags a.tag::text').getall()),
                        'text': " ".join([quote.css('span.text::text').get(),
                                    " by, ",
                                    quote.css('small.author::text').get()]),
                        'img': None
                    }
        except BaseException:
            pass

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
