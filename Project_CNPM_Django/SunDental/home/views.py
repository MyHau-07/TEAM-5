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
from .forms import DentistForm
from .decorators import role_required
from django.contrib.auth import logout
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
            if user.role == 'dentist':
                return redirect('dentist_dashboard')  # Đường dẫn đến dashboard của dentist
            elif user.role == 'clinic_owner':
                return redirect('clinic_owner_dashboard')  # Đường dẫn đến dashboard của clinic_owner
            else:
              # Đường dẫn đến dashboard của patient
                return redirect('patient_dashboard')
        else:
            messages.error(request, 'User  or password incorrect!')

    # Render the login page if GET request or login failed
    context = {}
    return render(request, 'home/includes/auth-login-basic.html', context)


@role_required('patient')
def patient_dashboard(request):
    # Logic cho dashboard của patient
    return render(request, 'home/home/patient_dashboard.html')

@role_required('dentist')
def dentist_dashboard(request):
    # Logic cho dashboard của dentist
    return render(request, 'home/home/dentist_dashboard.html')

@role_required('clinic_owner')
def clinic_owner_dashboard(request):
    # Logic cho dashboard của clinic_owner
    return render(request, 'home/home/clinic_owner_dashboard.html')
        


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


def custom_logout(request):
    logout(request)
    # Thêm logic tùy chỉnh nếu cần
    return redirect('home')


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