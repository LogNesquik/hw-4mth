from django.urls import path
from . import views

urlpatterns = [
    path('book_quote', views.book_quote),
    path('book_list/', views.book_list),
    path('book_list/<int:id>', views.book_detail),
    path('book_list/<int:id>/edit', views.update_book_qoute),
    path('book_list/<int:id>/delete', views.delete_book_qoute),

    path('create_book_qoute/', views.create_book_qoute)
]