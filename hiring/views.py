from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from . forms import CustomUserForm, LoginFormWithCaptcha
from hiring.forms import CustomUserForm

def register_view(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = CustomUserForm()

    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )

def login_view(request):
    if request.method == "POST":
        form = LoginFormWithCaptcha(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:

                login(request, user)
                return redirect('/profile/')
    else:
        form = LoginFormWithCaptcha()

    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )
def profile_view(request):
    return render(
        request, 
        'profile.html', 
        {
            'user': request.user
        }
    )


def logout_view(request):
    logout(request)
    return redirect('/login/')