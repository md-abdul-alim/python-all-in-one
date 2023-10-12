import subprocess
from django.conf import settings
from django.http import JsonResponse


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
