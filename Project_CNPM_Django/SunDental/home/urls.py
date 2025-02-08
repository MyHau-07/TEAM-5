from django.contrib import admin
from django.urls import include, path
from.import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('register/', views.register, name = 'register'),
    path('login_view/', views.login_view, name = 'login_view'),
    path('contact/', views.contact, name = 'contact'),
    path('search/', views.search, name = 'search'),

    
]