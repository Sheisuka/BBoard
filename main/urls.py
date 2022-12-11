from django.urls import path

from .views import index, other_page


urlpatterns = [
    path('<str:page>/', other_page, name='other_page'),
    path('', index, name='index'),
]