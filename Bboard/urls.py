from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('bboard/', include('main.urls')), # Переход на ссылки приложения bboard
    path('admin', admin.site.urls)
]
