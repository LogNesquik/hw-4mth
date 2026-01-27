from django.shortcuts import render
from django.http import HttpResponse

def book_quote(request):
    if request.method == "GET":
        return HttpResponse("Мысли великих людей — о жизненных ценностях, успехе и человеческих способностях")