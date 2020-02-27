import scrapy
import pandas as pd
import numpy as np
class PythonEventsSpider(scrapy.Spider):
	name = 'events'

	start_urls = ['https://www.python.org/events/python-events/',]

	def parse(self, response):
		for event in response.xpath('//ul[contains(@class, "list-recent-events")]/li'):
			yield {
			'name' : event.xpath('h3[@class="event-title"]/a/text()').extract_first(),
			'location' : event.xpath('p/span[@class="event-location"]/text()').extract_first(),
			'time': event.xpath('p/time/text()').extract_first(),
			}

