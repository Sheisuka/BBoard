from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404

from django.template import TemplateDoesNotExist
from django.template.loader import get_template

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, 
                                        PasswordResetView, PasswordResetConfirmView, 
                                        PasswordResetDoneView, PasswordResetCompleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView


from django.urls import reverse_lazy

from django.core.signing import BadSignature


from .utilities import signer
from .models import AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm


def index(request):
    return render(request, 'main/index.html')


def other_page(request, page):
    try:
        template = get_template(f'main/{page}.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    template_name = 'main/login.html'


class BBLogoutView(LogoutView, LoginRequiredMixin):
    template_name = 'main/logout.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class BBPasswordChangeView(PasswordChangeView, SuccessMessageMixin, LoginRequiredMixin):
    template_name = 'main/password_change.html'
    succes_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'
    

class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url  = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username) 
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class PasswordUserResetView(PasswordResetView):
    template_name = 'main/password_reset.html'


class PasswordUserResetConfirmationView(PasswordResetConfirmView):
    template_name = 'main/password_reset_confirm.html'


class PasswordUserResetDoneView(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'


class PasswordUserResetCompleteView(PasswordResetCompleteView):
    template_name = 'main/password_reset_complete.html'