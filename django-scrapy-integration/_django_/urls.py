
from django.contrib import admin
from django.urls import path
from .apis import run_scrapy_crawler, run_scrapy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lulu/', run_scrapy),
]
