from django.urls import path

from .views import index, other_page, BBLoginView


urlpatterns = [
    path('<str:page>/', other_page, name='other_page'),
    path('', index, name='index'),
    path('accounts/login/', BBLoginView.as_view(), name='login')
]