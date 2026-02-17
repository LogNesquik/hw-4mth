from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views import generic
from django.db.models import F
# crud
# create

class Search(generic.ListView):
    template_name = 'books_list.html'
    context_object_name = 'book_all'
    model = models.BookQuote

    def get_queryset(self):
        return self.model.objects.filter(title_books__icontains=self.request.GET.get('s'))
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context

class CreateBookQoute(generic.CreateView):
    template_name = 'create_book_qoute.html'
    form_class = forms.BookQuoteForms
    success_url = '/books/'

    def form_valid(self, form):
        print(form.changed_data)
        return super(CreateBookQoute, self).form_valid(form=form)

class UpdateBookQoute(generic.UpdateView):
    template_name = 'update_book_qoute.html'
    form_class = forms.BookQuoteForms
    model = models.BookQuote
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_qoute_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_qoute_id)

    def form_valid(self, form):
        print(form.changed_data)
        return super(UpdateBookQoute, self).form_valid(form=form)

class DeleteBookQoute(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/books/'
    model = models.BookQuote
    context_object_name = 'BookQoute'

    def get_object(self, **kwargs):
        book_quote_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=book_quote_id)

class BookListQoute(generic.ListView):
    template_name = 'books_list.html'
    model = models.BookQuote
    context_object_name = 'book_all'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookDetailQoute(generic.DetailView):
    template_name = 'books_detail.html'
    context_object_name = 'book_detail_id'
    model = models.BookQuote




# Это можно и не менять
def book_quote(request):
    if request.method == "GET":
        return HttpResponse("Мысли великих людей — о жизненных ценностях, успехе и человеческих способностях")
    
class BookDetailView(generic.DetailView):
    template_name = 'books_detail.html'
    context_object_name = 'book_id'
    pk_url_kwarg = 'id'
    model = models.BookQuote