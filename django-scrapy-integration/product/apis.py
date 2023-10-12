import subprocess
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from .models import Product
from .serializers import ProductSerializer
import csv


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
            response['Content-Disposition'] = 'attachment; filename="data.csv"'

            # Create a CSV writer and write your data into the response.
            writer = csv.writer(response)
            writer.writerow(['Id', 'Title', 'Price'])

            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
            for i in serializer.data:
                writer.writerow([i['id'], i['title'], i['price']])

            return response

    except Exception as e:
        response_data = {
            'status': 'error',
            'message': 'An error occurred while running the Scrapy crawler.',
            'error_message': str(e)
        }

        return JsonResponse(response_data)
