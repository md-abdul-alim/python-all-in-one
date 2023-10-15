import subprocess
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Product
from .serializers import ProductSerializer
import csv

"""
subprocess
-----run()
---------- Synchronous
---------- High-level blocking function, means waits for the subprocess to finish before continuing with other tasks.
-------------------- Follow: run_scrapy_crawler_by_run()
-----Popen()
---------- Asynchronous
---------- Use for multiple process concurrently and interacting with long-running process.
-------------------- Follow: run_multiple_scrapy_crawler_popen_multiple_processes_concurrently()
---------- Lower-level non-blocking functions, means start the subprocess and continue with other tasks. Doesn't wait for the the subprocess complete.
-------------------- Follow: run_scrapy_crawler_by_popen()
---------- If want to wait like run(), use `wait()` popen method. 
-------------------- Follow: run_scrapy_crawler_by_popen_as_run()
---------- Using `Poll()`, until Popen() complete the task we can do some other tasks.
-------------------- Follow: run_scrapy_crawler_by_popen_and_do_some_other_tasks()
---------- There are lots of function. Like stdout, stderr
"""


@require_http_methods(["GET"])
def run_scrapy_crawler_by_run(request):
    spider_name = 'luluspider'

    try:
        process = subprocess.run(['scrapy', 'crawl', spider_name], cwd=settings.SPIDER_DIRECTORY)
        if process.returncode == 0:
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


@require_http_methods(["GET"])
def run_scrapy_crawler_by_popen(request):
    spider_name = 'luluspider'

    try:
        process = subprocess.Popen(['scrapy', 'crawl', spider_name], cwd=settings.SPIDER_DIRECTORY)

        # Check if the process is still running
        while process.poll() is None:
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


@require_http_methods(["GET"])
def run_scrapy_crawler_by_popen_as_run(request):
    spider_name = 'luluspider'

    try:
        process = subprocess.Popen(['scrapy', 'crawl', spider_name], cwd=settings.SPIDER_DIRECTORY)

        process.wait()

        if process.returncode == 0:
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


@require_http_methods(["GET"])
def run_scrapy_crawler_by_popen_and_do_some_other_tasks(request):
    spider_name = 'luluspider'

    try:
        process = subprocess.Popen(['scrapy', 'crawl', spider_name], cwd=settings.SPIDER_DIRECTORY)

        while process.poll() is None:
            # We can perform other tasks or wait
            print('------Doing some other tasks------')
            pass

        if process.returncode == 0:
            response_data = {
                'status': 'success',
                'message': 'Scrapy crawler executed successfully.'
            }
            return JsonResponse(response_data)
        else:
            response_data = {
                'status': 'failed',
                'message': f"Process returned an error. Return code: {process.returncode}"
            }
            return JsonResponse(response_data)

    except Exception as e:
        response_data = {
            'status': 'error',
            'message': 'An error occurred while running the Scrapy crawler.',
            'error_message': str(e)
        }

        return JsonResponse(response_data)


@require_http_methods(["GET"])
def run_multiple_scrapy_crawler_popen_multiple_processes_concurrently(request):
    spider_name = 'luluspider'
    # TODO : Spider running infinity . Need to fix.
    commands = [
        ["echo", "Process 1"],
        ["echo", "Process 2"],
        ['scrapy', 'crawl', spider_name],
        ['scrapy', 'crawl', 'wrong spider name'],
    ]

    processes = []
    try:
        for cmd in commands:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=settings.SPIDER_DIRECTORY)
            processes.append(process)

        # for process in processes:
        #     process.wait()

        success = []
        fail = []
        # Collect and print the output of each process
        for i, process in enumerate(processes):
            stdout, stderr = process.communicate()
            print(f"Process {i + 1} output: ", stdout, stderr)
            if stdout:
                success.append((f"Process {i + 1} output: ", stdout))
            if stderr:
                fail.append((f"Process {i + 1} output: ", stderr))

        response_data = {
            'status': 'success',
            'message': 'Multiple process executed successfully.',
            'data': success,
            'fail': fail
        }
        return JsonResponse(response_data)
    except Exception as e:
        response_data = {
            'status': 'error',
            'message': 'An error occurred while running the Scrapy crawler.',
            'error_message': str(e)
        }

        return JsonResponse(response_data)
"""
cwd: current working directory

"""