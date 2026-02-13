from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_quote, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/<int:id>/edit/', views.update_book_qoute, name='book_edit'),
    path('books/<int:id>/delete/', views.delete_book_qoute, name='book_delete'),
    path('books/create/', views.create_book_qoute, name='book_create'),
    path('search/', views.search_view, name='search'),
]