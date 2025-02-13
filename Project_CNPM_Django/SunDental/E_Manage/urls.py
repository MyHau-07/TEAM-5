from django.contrib import admin
from django.urls import path, include
from.import views
from .views import them_vao_gio_hang, xoa_khoi_gio_hang, sua_so_luong
urlpatterns = [
    path('uudai', views.uudai, name="uudai"),
    path('sukien', views.sukien, name="sukien"),
    path('kienthuc', views.kienthuc, name= "kienthuc"),
    path('user/', views.user, name="user"),
    path('giohang', views.giohang, name = "giohang"),
    path('news', views.news, name="news"),
    path('booking', views.booking, name = "booking"),
    path('dentist', views.Dentist, name = "Dentist"),
    path('dichvu', views.dichvu, name = "dichvu"),
    path('chamcong', views.chamcong, name = "chamcong"),
    path('nghiphep', views.nghiphep, name = "nghiphep"),
    path('lichlam', views.lichlam, name = "lichlam"),
    path('lichhen', views.lichhen, name = "lichhen"),
    path('lichsu', views.lichsu, name = "lichsu"),
    path('myuudai', views.myuudai, name = "myuudai"),
    #clicnicowner
    path('ClicnicOwner', views.ClicnicOwner, name = "ClicnicOwner"),
    #quan li phong kham
     path('hosophongkham', views.hosophongkham, name = "hosophongkham"),
    # quan li chi nhanh
    path('quanlichinhanh', views.quanlichinhanh, name = "quanlichinhanh"),
    # quan li nhan vien
    path('quanlinhanvien', views.quanlinhanvien, name = "quanlinhanvien"),
    # quan li dich vu
    path('quanlidichvu', views.quanlidichvu, name = "quanlidichvu"),
    # Thêm dịch vụ vào giỏ hàng
    path('them/<int:dich_vu_id>/', views.them_vao_gio_hang, name='them_vao_gio_hang'),
    
    # Xóa dịch vụ khỏi giỏ hàng
    path('xoa_khoi_gio_hang/<int:item_id>/', views.xoa_khoi_gio_hang, name='xoa_khoi_gio_hang'),
    
    # Sửa số lượng trong giỏ hàng
    path('sua/<int:gio_hang_id>/', views.sua_so_luong, name='sua_so_luong'),

    
    # them dich vu
    path('manage/cart/<int:dich_vu_id>/add/', views.add_to_cart, name='add_to_cart'),

    
    # Thanh toán giỏ hàng
    path('thanh-toan/', views.thanh_toan, name='thanh_toan'),
    
]

