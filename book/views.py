from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
# crud
# create
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
            return redirect('/book_list/')
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
    return redirect('/book_list/')

def book_quote(request):
    if request.method == "GET":
        return HttpResponse("Мысли великих людей — о жизненных ценностях, успехе и человеческих способностях")

# read
def book_list(request):
    if request.method == 'GET':
        book_all = models.BookQuote.objects.all()
        return render(
            request,
            'books_list.html',
            {
                'book_all': book_all
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