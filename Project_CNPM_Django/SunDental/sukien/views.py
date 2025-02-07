from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sukien (request):
    return render(request, 'sukien.html')