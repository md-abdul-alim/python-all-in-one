from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book/', include('bookAuthor.urls')),
    path('api/social/', include('socialMedia.urls')),

]
