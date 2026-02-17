from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.AuthLoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.AuthLogoutView.as_view()),
]