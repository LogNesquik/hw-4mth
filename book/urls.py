from django.urls import path
from . import views

urlpatterns = [
    path('book_quote', views.book_quote),
    path('book_list', views.book_list),
    path('book_list/<int:id>', views.book_detail),
]