from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from E_Manage.models import Services
from .forms import Comment_Form
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.

def home (request):
    services = Services.objects.filter(is_active=True)
    
    # Chia services thành các nhóm 5 item cho mỗi carousel-item
    grouped_services = [services[i:i+5] for i in range(0, len(services), 5)]
    return render(request, 'home/home/home.html', {
        'grouped_services': grouped_services
    })

def login_view(request):
    # Redirect to home if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('home')

    # Handle POST request for login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, 'User  or password incorrect!')

    # Render the login page if GET request or login failed
    context = {}
    return render(request, 'home/includes/auth-login-basic.html', context)
        


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login_view')  # Đổi 'login' thành URL của trang đăng nhập của bạn
    else:
        form = SignUpForm()

    return render(request, 'home/includes/auth-register-basic.html', {'form': form})

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = Comment_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = Comment_Form()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/includes/contact.html', {'form': form, 'submitted': submitted})


def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')
        services = Services.objects.filter(name__contains=searched)
        return render(request, 'home/includes/search.html', {'searched':searched,
                                                             'services':services})
    else:
        return render(request, 'home/includes/search.html', {})