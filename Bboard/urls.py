from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
import Bboard.settings as settings

from main.views import PasswordUserResetView, PasswordUserResetConfirmationView, PasswordUserResetDoneView, PasswordUserResetCompleteView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('main.urls')), # Переход на ссылки приложения bboard
    path('accounts/password/reset/', PasswordUserResetView.as_view(), name='password_reset'),
    path('accounts/password/reset/<str:uidb64>/<str:token>/', PasswordUserResetConfirmationView.as_view(), name='password_reset_confirm'),
    path('accounts/password/reset/done/', PasswordUserResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password/reset/complete', PasswordUserResetCompleteView.as_view(), name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
