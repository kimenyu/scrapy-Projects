import scrapy
from ..items import JumiaItem

class Jumiaspider(scrapy.Spider):
    name = 'jumia'
    start_urls = [
        "https://www.jumia.co.ke/smartphones/"
    ]


    

    def parse(self, response):
        items = JumiaItem()
        #all_phones = response.css(".-elli::text")
        
        #for phones in all_phones:
        name = response.css(".name::text").extract()
        price =response.css(".prc::text").extract()
            
            
        items['name'] = name
        items['price'] = price
        
        yield items
        
