import scrapy



class BlogSpider(scrapy.Spider):
	name = "blogscraper"

	start_urls = [
		"https://gopalpanwar.tech/blog/",
		"https://gopalpanwar.tech/random-forest-regression/"
	]

	# def start_requests(self):
	# 	for url in urls:
	# 		yield scrapy.Request(url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = f"page_{page}.html"

		with open(filename, "wb") as f:
			f.write(response.body)
		self.log(f"File {filename} has been saved.")
		
