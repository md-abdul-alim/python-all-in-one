import environ
import os
import sys
from pathlib import Path

# import .env file
env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)

# import django settings
sys.path.append(env('DJANGO_DIRECTORY'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", '_django_.settings')
import django
django.setup()

from product.models import Product
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

class LuluscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()


class DjangoScraperItem(DjangoItem):
    django_model = Product

