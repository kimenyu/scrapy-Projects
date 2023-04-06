import scrapy
from .. items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	page_number = 2
	start_urls = [
		'http://quotes.toscrape.com/page/1/'
	]

	def parse(self, response):
		items = QuotetutorialItem()

		all_qoutes = response.css('.quote')
		for quotes in all_qoutes:
			titles= quotes.css('.text::text').extract()
			authors = quotes.css('.author::text').extract()
			tag = quotes.css('.tag::text').extract()

			items['titles'] = titles
			items['authors'] = authors
			items['tags'] = tag

			yield items
		# next_page = response.css('li.next a::attr(href)').get()

		# if next_page is not None:
		# 	yield response.follow(next_page, callback= self.parse)
		next_page = 'http://quotes.toscrape.com/page/' + str(self.page_number) + '/'
		if self.page_number < 11:
			self.page_number += 1
			yield response.follow(next_page, callback=self.parse)