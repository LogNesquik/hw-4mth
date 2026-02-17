from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . forms import CustomUserForm, LoginFormWithCaptcha
from hiring.forms import CustomUserForm
from django.views import generic
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView

class RegisterView(generic.CreateView):
    template_name = 'register.html'
    form_class = CustomUserForm
    success_url = '/login/'

class AuthLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginFormWithCaptcha


    def get_success_url(self):
        return reverse('profile')

class ProfileView(generic.TemplateView):
    template_name = 'profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class AuthLogoutView(LogoutView):
    next_page = '/login/'