from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'login_app/login.html'

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'login_app/home.html'

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'login_app/login.html'