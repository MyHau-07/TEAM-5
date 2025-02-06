from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Dentist (request):
    return render(request, 'Dentist/Dentist.html')