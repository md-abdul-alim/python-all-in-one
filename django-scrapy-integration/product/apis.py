import subprocess
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Product
from .serializers import ProductSerializer
import csv

@require_http_methods(["GET"])
def run_scrapy_crawler(request):
    spider_name = 'luluspider'

    try:
        process = subprocess.run(['scrapy', 'crawl', spider_name], cwd=settings.SPIDER_DIRECTORY)
        if process.returncode == 0:
            # response_data = {
            #     'status': 'success',
            #     'message': 'Scrapy crawler executed successfully.'
            # }
            # return JsonResponse(response_data)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="lulu.csv"'

            # Create a CSV writer and write your data into the response.
            writer = csv.writer(response)
            writer.writerow(['Title', 'Price'])

            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            for i in serializer.data:
                writer.writerow([i['title'], i['price']])

            return response

    except Exception as e:
        response_data = {
            'status': 'error',
            'message': 'An error occurred while running the Scrapy crawler.',
            'error_message': str(e)
        }

        return JsonResponse(response_data)