from django.urls import path
from .apis import (run_scrapy_crawler_by_run, run_scrapy_crawler_by_popen, run_scrapy_crawler_by_popen_as_run,
                   run_scrapy_crawler_by_popen_and_do_some_other_tasks,
                   run_multiple_scrapy_crawler_popen_multiple_processes_concurrently)

urlpatterns = [
    path('lulu/run/', run_scrapy_crawler_by_run),  # start the crawler in wait for the execution finish
    path('lulu/popen/', run_scrapy_crawler_by_popen),  # just start the crawler,no need to wait for the execution finish
    path('lulu/use_popen_as_run/', run_scrapy_crawler_by_popen_as_run),
    path('lulu/popen_with_multi_tasks/', run_scrapy_crawler_by_popen_and_do_some_other_tasks),
    path('lulu/popen_multi_processes/', run_multiple_scrapy_crawler_popen_multiple_processes_concurrently),
]
