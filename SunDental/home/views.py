from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from kienthuc.models import Kienthuc

# # Create your views here.

def home (request):
    return render(request, 'home/home/giohang.html')

def register(request):
    return render(request, 'home/includes/auth-register-basic.html')   

# def kien_thuc(request):
#     return render(request, 'home/includes/kien_thuc.html') 

def Trangkienthuc(request):
  mykienthuc = Kienthuc.objects.get(id=1)
  template = loader.get_template('home/home/kien_thuc.html')
  context = {
    'mykienthuc': mykienthuc,
  }
  return HttpResponse(template.render(context, request))

def giohang(request):
  mygiohang = giohang.objects.get(id=1)
  template = loader.get_template('home/home/user.html')
  context = {
    'mygiohang': mygiohang,
  }
  return HttpResponse(template.render(context, request))







