from django.shortcuts import render
from django.http import HttpResponse


def kien_thuc(request):
    return render(request, 'home/home/kien_thuc.html') 