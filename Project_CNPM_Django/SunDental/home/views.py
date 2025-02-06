from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home (request):
    return render(request, 'home/home/home.html')

def register(request):
    return render(request, 'home/includes/auth-register-basic.html')    


def contact(request):
    return render(request, 'home/includes/contact.html')   
