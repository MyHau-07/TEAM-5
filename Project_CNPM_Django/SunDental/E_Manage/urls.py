from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('uudai', views.uudai, name="uudai"),
    path('sukien', views.sukien, name="sukien"),
    path('kienthuc', views.kienthuc, name= "kienthuc"),
    path('user/', views.user, name="user"),
    path('booking', views.booking, name = "booking"),
    path('dentist', views.dentist, name = "dentist"),
    path('dichvu', views.dichvu, name = "dichvu"),
    path('chamcong', views.chamcong, name = "chamcong"),
    path('nghiphep', views.nghiphep, name = "nghiphep"),
    # path('lichlam/', views.lichlam, name = "lichlam"),
    
    path('lichsu', views.lichsu, name = "lichsu"),
    path('lichhenbs', views.appointment, name = "lichhenbs"),
    path('ClicnicOwner', views.ClicnicOwner, name = "ClicnicOwner"),
    path('hosophongkham', views.hosophongkham, name = "hosophongkham"),
    path('quanlichinhanh', views.quanlichinhanh, name = "quanlichinhanh"),
    path('quanlidichvu', views.quanlidichvu, name = "quanlidichvu"),
    path('quanlinhanvien', views.quanlinhanvien, name = "quanlinhanvien"),
    path('quanlithongtinbenhnhan', views.quanlithongtinbenhnhan, name = "quanlithongtinbenhnhan"),
    path('hosobenhan/<int:record_id>/', views.hosobenhan_detail, name='hosobenhan_detail'),
    #cap nhat lich hen
    path('lichhen/', views.lichhen , name='lichhen'),
    path('update-appointment/', views.update_appointment_status, name='update_appointment'),
    #lich lam
    path('lichlam/', views.lichlam, name='lichlam'),
    path('GioHang', views.Gio_Hang, name = "GioHang"),
    path('them/<int:dich_vu_id>/', views.them_vao_gio_hang, name='them_vao_gio_hang'),
    path('xoa_khoi_gio_hang/<int:item_id>/', views.xoa_khoi_gio_hang, name='xoa_khoi_gio_hang'),
    # path('sua/<int:gio_hang_id>/', views.sua_so_luong, name='sua_so_luong'),
    path('sua_so_luong/<int:gio_hang_id>/', views.sua_so_luong, name='sua_so_luong'),
    path('manage/cart/<int:dich_vu_id>/add/', views.add_to_cart, name='add_to_cart'),
    path('thanh-toan/', views.thanh_toan, name='thanh_toan'),
]