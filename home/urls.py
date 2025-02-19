from django.contrib import admin
from django.urls import include, path
from.import views
from .views import custom_logout
urlpatterns = [
    path('', views.home, name = "home"),
    path('register/', views.register, name = 'register'),
    path('login_view/', views.login_view, name = 'login_view'),
    path('contact/', views.contact, name = 'contact'),
    path('search/', views.search, name = 'search'),
    path('patient_dashboard', views.patient_dashboard, name = "patient_dashboard"),
    path('dentist_dashboard', views.dentist_dashboard, name = "dentist_dashboard"),
    path('clinic_owner_dashboard', views.clinic_owner_dashboard, name = "clinic_owner_dashboard"),
    path('logout/', custom_logout, name='logout'),
    
   
    
]