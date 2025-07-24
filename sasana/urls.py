from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_sasana, name='input_sasana'),
    path('terdekat/', views.cari_sasana_terdekat, name='cari_sasana_terdekat'),
]