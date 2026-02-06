from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_category, name='pro'),
    path('categories/', views.list_category, name='category_list'),
    path('category/<int:id>/', views.category_product, name='category_products')
]