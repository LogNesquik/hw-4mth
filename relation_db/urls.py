from django.urls import path
from . import views

urlpatterns = [
    path('all_tour/', views.relation_db)
]