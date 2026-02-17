from django.urls import path
from . import views

urlpatterns = [
    path('all_tour/', views.RelationDBView.as_view(), name='relation_db'),
]