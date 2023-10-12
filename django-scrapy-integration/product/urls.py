from django.urls import path
from .apis import run_scrapy_crawler, run_scrapy

urlpatterns = [
    path('lulu/', run_scrapy_crawler),
]
