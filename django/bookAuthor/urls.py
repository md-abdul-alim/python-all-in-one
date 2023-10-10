from django.urls import path
from bookAuthor.apis import GetBookByAuthor

urlpatterns = [
    path('get/book/by/author/', GetBookByAuthor.as_view())
]
