from django.shortcuts import render
from . import models

def relation_db(request):
    if request.method == 'GET':
        choice_tour = models.Person.objects.all()
    return render(
        request,
        'relation_db.html',
        {
            'choice_tour': choice_tour
        }
    )
# Create your views here.
