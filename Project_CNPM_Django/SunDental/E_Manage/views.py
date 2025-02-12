from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from home.forms import CustomUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def user (request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Cập nhật thông tin thành công!")
            return redirect('user')  # Reload the profile page after saving the data
        else:
            # Thông báo lỗi nếu form không hợp lệ
            messages.error(request, "Đã có lỗi xảy ra. Vui lòng thử lại.")
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'Users/user.html', {'user': user, 'form': form})

def giohang (request):
    return render(request, 'Pages/giohang.html')

def news (request):
    return render(request, 'Pages/news.html')

def booking (request):
    return render(request, 'Pages/booking.html')

def dentist (request):
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