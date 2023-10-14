from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from luluscraper import settings as my_settings
from luluscraper.spiders.luluspider import LuluspiderSpider


class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(LuluspiderSpider)
        process.start()
