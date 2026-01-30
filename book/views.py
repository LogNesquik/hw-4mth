from django.shortcuts import render, get_object_or_404
from . import models
from django.http import HttpResponse

def book_quote(request):
    if request.method == "GET":
        return HttpResponse("Мысли великих людей — о жизненных ценностях, успехе и человеческих способностях")


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