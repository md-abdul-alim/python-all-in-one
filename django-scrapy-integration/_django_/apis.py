from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from luluscraper.luluscraper.spiders.luluspider import LuluspiderSpider
from django.http import HttpResponse
from twisted.internet import threads
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
    # Define the Scrapy spider name (replace 'myspider' with your spider's name)
    spider_name = 'luluspider'

    # Run the Scrapy spider as a subprocess
    try:
        process = subprocess.Popen(['scrapy', 'crawl', spider_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            response_data = {
                'status': 'success',
                'message': 'Scrapy crawler executed successfully.'
            }
        else:
            response_data = {
                'status': 'error',
                'message': 'Scrapy crawler encountered an error.',
                'error_message': stderr.decode()
            }
    except Exception as e:
        response_data = {
            'status': 'error',
            'message': 'An error occurred while running the Scrapy crawler.',
            'error_message': str(e)
        }

    return JsonResponse(response_data)
