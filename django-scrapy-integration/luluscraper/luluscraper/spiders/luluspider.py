import scrapy


class LuluspiderSpider(scrapy.Spider):
    name = "luluspider"
    allowed_domains = ["www.luluhypermarket.com"]
    start_urls = ["https://www.luluhypermarket.com/en-ae/electronics"]

    def parse(self, response):
        sub_categories = response.css('section.recommended-for-you div.col-lg-2')

        for sub_category in sub_categories:
            relative_url = sub_category.css('div.col-lg-2 a').attrib['href']
            sub_category_url = "https://www.luluhypermarket.com/en-ae" + relative_url
