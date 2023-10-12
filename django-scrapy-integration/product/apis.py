from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from luluscraper.spiders.luluspider import LuluspiderSpider
from django.http import HttpResponse
from django.conf import settings
import subprocess
from django.http import JsonResponse

def run_scrapy(request):
    try:
        process = CrawlerProcess(get_project_settings())
        process.crawl(LuluspiderSpider)
        process.start()
    except Exception as e:
        response_data = {
            'error_message': str(e)
        }
        return JsonResponse(response_data)

    # d = threads.deferToThread(run_scrapy)

    return HttpResponse("Scrapy spider is running.")


def run_scrapy_crawler(request):
    spider_name = 'luluspider'

    try:
        process = subprocess.run(['scrapy', 'crawl', spider_name], cwd=settings.SPIDER_DIRECTORY)
        if process.returncode == 0:
            response_data = {
                'status': 'success',
                'message': 'Scrapy crawler executed successfully.'
            }
            return JsonResponse(response_data)

    except Exception as e:
        response_data = {
            'status': 'error',
            'message': 'An error occurred while running the Scrapy crawler.',
            'error_message': str(e)
        }

        return JsonResponse(response_data)
