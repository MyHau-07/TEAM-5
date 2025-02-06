from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('uudai/', views.uudai, name="uudai"),
    path('sukien/', views.sukien, name="sukien"),
    path('kienthuc/', views.kienthuc, name= "kienthuc"),
    path('user/', views.user, name="user"),
    path('giohang/', views.giohang, name = "giohang"),
    path('news/', views.news, name="news"),
    path('booking/', views.booking, name = "booking"),
    path('dentist/', views.Dentist, name = "Dentist"),
    path('dichvu/', views.dichvu, name = "dichvu"),
]