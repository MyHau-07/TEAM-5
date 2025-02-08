from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user (request):
    return render(request, 'Users/user.html')

def giohang (request):
    return render(request, 'Pages/giohang.html')

def news (request):
    return render(request, 'Pages/news.html')

def booking (request):
    return render(request, 'Pages/booking.html')

def Dentist (request):
    return render(request, 'Users/Dentist.html')

def chamcong (request):
    return render(request, 'Users/chamcong.html')

def nghiphep (request):
    return render(request, 'Users/nghiphep.html')

def lichlam (request):
    return render(request, 'Users/lichlam.html')

def lichhen (request):
    return render(request, 'Users/lichhen.html')

def lichsu (request):
    return render(request, 'Users/lichsu.html')

def myuudai (request):
    return render(request, 'Users/myuudai.html')

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