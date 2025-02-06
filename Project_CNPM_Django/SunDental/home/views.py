from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from E_Manage.models import Services
# Create your views here.

def home (request):
    return render(request, 'home/home/home.html')

def register(request):
    return render(request, 'home/includes/auth-register-basic.html')    


def contact(request):
    return render(request, 'home/includes/contact.html')   


def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        services = Services.objects.filter(name__contains=searched)
        return render(request, 'home/includes/search.html', {'searched':searched,
                                                             'services':services})
    else:
        return render(request, 'home/includes/search.html', {})

