from django.shortcuts import render
from . import models
from django.views import generic


class RelationDBView(generic.TemplateView):
    template_name = 'relation_db.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choice_tour'] = models.Person.objects.all()
        return context