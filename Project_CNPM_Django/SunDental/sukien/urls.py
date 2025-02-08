from django.contrib import admin
from django.urls import path, include
from.import views
urlpatterns = [
    path('sukien/', views.sukien, name="sukien"),
   
]
