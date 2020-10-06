from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Earring',views.Earring,name='Earring'),
    path('Necklace',views.Necklace,name='Necklace'),
    path('Bracelet',views.Bracelet,name='Bracelet'),


    
]
