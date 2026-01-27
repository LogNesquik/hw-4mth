from django.urls import path
from . import views

urlpatterns = [
    path('book_quote', views.book_quote)
]