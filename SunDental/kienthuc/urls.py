from django.contrib import admin
from django.urls import include, path
from.import views
urlpatterns = [
   
    path('kien_thuc/', views.kien_thuc, name = 'kien_thuc'),
    
]