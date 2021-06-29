import scrapy

class Quote_slider(scrapy.Spider):
    name="quotes"
    start_urls=[
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response, **kwargs):
        all_div_quotes=response.css('div.quote')
        
        for quotes in all_div_quotes:
            title=quotes.css('span.text::text').extract()
            author=quotes.css('small.author::text').extract()
            tags=quotes.css('div.tags a.tag::text').extract()
            yield {
                "title":title,
                "author":author,
                "tags":tags
            }
   