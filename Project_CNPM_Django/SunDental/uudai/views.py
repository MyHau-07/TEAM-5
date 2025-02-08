from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def uudai (request):
    return render(request, 'uudai.html')