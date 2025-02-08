from django.contrib import admin
from django.urls import include, path
from.import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('register/', views.register, name = 'register'),
    path('login/', views.register, name = 'login'),
    path('contact/', views.contact, name = 'contact'),
    path('search/', views.search, name = 'search'),
    path('dichvu/', views.dichvu, name = 'dichvu'),
    
]