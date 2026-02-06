from django.shortcuts import render, get_object_or_404
from . import models

def product_category(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        return render(
            request,
            'products.html',
            {
                'products': products
            }
        )
    
def list_category(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        return render(
            request,
            'categories.html',
            {
                'categories': categories
            }
        )
    
def category_product(request, id):
    if request.method == 'GET':
        category = get_object_or_404(models.Category, id=id)
        products = category.tags.all()
        return render(
            request,
            'category_products.html',
            {
                'category': category,
                'products': products
            }
        )
# Create your views here.
