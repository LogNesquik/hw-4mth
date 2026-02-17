from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_quote, name='home'),
    path('books/', views.BookListQoute.as_view(), name='book_list'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/<int:id>/edit/', views.UpdateBookQoute.as_view(), name='book_edit'),
    path('books/<int:id>/delete/', views.DeleteBookQoute.as_view(), name='book_delete'),
    path('books/create/', views.CreateBookQoute.as_view(), name='book_create'),
    path('search/', views.Search.as_view(), name='search'),
]