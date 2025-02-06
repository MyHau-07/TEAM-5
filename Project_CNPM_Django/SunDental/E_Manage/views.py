from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user (request):
    return render(request, 'Pages/user.html')

def giohang (request):
    return render(request, 'Pages/giohang.html')

def news (request):
    return render(request, 'Pages/news.html')

def booking (request):
    return render(request, 'Pages/booking.html')

def Dentist (request):
    return render(request, 'Pages/Dentist.html')

#----left menu
def dichvu (request):
    return render(request, 'Pages/dichvu.html')

def uudai (request):
    return render(request, 'Pages/uudai.html')

def sukien (request):
    return render(request, 'Pages/sukien.html')  

def kienthuc (request):
    return render(request, 'Pages/kienthuc.html')
#left menu---