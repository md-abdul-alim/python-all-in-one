# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
# from product.models import Product


class LuluscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()


# class DjangoScraperItem(DjangoItem):
#     django_model = Product

