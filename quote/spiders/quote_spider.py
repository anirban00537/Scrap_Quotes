import scrapy
from ..items import QuoteItem

class Quote_slider(scrapy.Spider):
    name="quotes"
    start_urls=[
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response, **kwargs):
        # all_div_quotes=response.css('div.quote')
        
        # items=QuoteItem()
        
        # for quotes in all_div_quotes:
        #     title=quotes.css('span.text::text').extract()
        #     author=quotes.css('small.author::text').extract()
        #     tags=quotes.css('div.tags a.tag::text').extract()
        #     items['title']=title
        #     items['author']=author
        #     items['tags']=tags
        #     yield items
         
        all_div_quotes=response.css('div.quote')
        for oneQuote in all_div_quotes:
            title=oneQuote.css('div span.text::text').extract()
            author=oneQuote.css('small.author::text').extract()
            tags=oneQuote.css('div.tags a.tag::text').extract()
            yield{
                "title":title,
                "author":author,
                "tags":tags
            }
        next_page_url=response.css("li.next a::attr(href)").extract()
        if next_page_url is not None:
            next_page_url= response.urljoin(next_page_url[0])
            yield scrapy.Request(next_page_url,callback=self.parse)
