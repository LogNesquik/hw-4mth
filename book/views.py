from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.core.paginator import Paginator
# crud
# create

def search_view(request):
    query = request.GET.get('s', '')
    if query:
        book_all = models.BookQuote.objects.filter(title_books__icontains=query)
    else:
        book_all = models.BookQuote.objects.none()
    return render(
        request,
        'books_list.html',
        {
            'book_all': book_all
        }
    )

def create_book_qoute(request):
    if request.method == 'POST':
        form = forms.BookQuoteForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/book_list/')
    else:
        form = forms.BookQuoteForms()
    return render(
        request,
        'create_book_qoute.html',
        {
            'form': form
        }
    )

def update_book_qoute(request, id):
    book_qoute_id = get_object_or_404(models.BookQuote, id=id)
    if request.method == "POST":
        form = forms.BookQuoteForms(request.POST, instance=book_qoute_id)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = forms.BookQuoteForms(instance=book_qoute_id)
    return render(
        request,
        'update_book_qoute.html',
        {
            'form': form,
            'book_qoute_id': book_qoute_id
        }
    )

def delete_book_qoute(request, id):
    book_qoute_id = get_object_or_404(models.BookQuote, id=id)
    book_qoute_id.delete()
    return redirect('/books/')

def book_quote(request):
    if request.method == "GET":
        return HttpResponse("Мысли великих людей — о жизненных ценностях, успехе и человеческих способностях")

# read
def book_list(request):
    if request.method == 'GET':
        book_all = models.BookQuote.objects.all()
        paginator = Paginator(book_all, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        return render(
            request,
            'books_list.html',
            {
                'book_all': page_obj
            }
        )
    
def book_detail(request, id):
    if request.method == 'GET':
        book_detail_id = get_object_or_404(models.BookQuote, id=id)
        return render(
            request,
            'books_detail.html',
            {
                'book_id': book_detail_id
            }
        )