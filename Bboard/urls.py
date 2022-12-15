from django.contrib import admin
from django.urls import path, include
from main.views import (index, BBLoginView, other_page, profile, BBLogoutView, 
                        ChangeUserInfoView, BBPasswordChangeView, 
                        RegisterDoneView, RegisterUserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bboard/', include('main.urls')),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other_page'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register')
]
