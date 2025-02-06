from django.shortcuts import render
from django.http import HttpResponse


def giohang(request):
    return render(request, 'home/home/giohang.html') 