from django.contrib import admin
from django.urls import include, path
from.import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('register/', views.register, name = 'register'),
    path('login/', views.register, name = 'login'),
    path('Trangkienthuc/', views.Trangkienthuc, name = 'Trangkienthuc'),
    path('giohang/', views.giohang, name = 'giohang'),

    path('tay-trang-nha-khoa/', views.taytrangnhakhoa, name = 'tay-trang-nha-khoa'),
    path('lichlam/', views.lichlam, name = 'lichlam'),
    path('cham-cong/', views.chamcong, name = 'cham-cong'),
    path('nghi-phep/', views.nghiphep, name = 'nghi-phep'),


    

]