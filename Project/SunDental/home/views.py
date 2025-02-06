from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home (request):
    return render(request, 'home/home/home.html')

def register(request):
    return render(request, 'home/includes/auth-register-basic.html')  
  
def service_view(request):
    return render(request, 'home/home/service.html')

def news_view(request):
    return render(request, 'home/home/news.html')

def contact_view(request):
    return render(request, 'home/home/contact.html')

def event_view(request):
    return render(request, 'home/home/event.html')

def learning_view(request):
    return render(request, 'home/home/learning.html')

def service_view(request):
    return render(request, 'home/home/service.html')