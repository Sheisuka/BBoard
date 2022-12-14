from django.contrib import admin
from django.urls import path
from main.views import (BBLoginView, other_page, profile, BBLogoutView, 
                        ChangeUserInfoView, BBPasswordChangeView, 
                        RegisterDoneView, RegisterUserView, user_activate, DeleteUserView,
                        PasswordUserResetConfirmationView, PasswordUserResetView)

from .views import index, by_rubric

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),

    path('<int:pk>/', by_rubric, name='by_rubric'),

    path('<str:page>/', other_page, name='other_page'), # Единичные страницы

    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),

    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/delete', DeleteUserView.as_view(), name='profile_delete'),

    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),

    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
]