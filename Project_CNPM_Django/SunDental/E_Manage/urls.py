from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('uudai', views.uudai, name="uudai"),
    path('sukien', views.sukien, name="sukien"),
    path('kienthuc', views.kienthuc, name= "kienthuc"),
    path('user/', views.user, name="user"),
    
    path('booking', views.booking, name = "booking"),
    path('dichvu', views.dichvu, name = "dichvu"),
    path('chamcong', views.chamcong, name = "chamcong"),
    path('nghiphep', views.nghiphep, name = "nghiphep"),
    path('lichlam', views.lichlam, name = "lichlam"),
    path('lichhen', views.lichhen, name = "lichhen"),
    path('lichsu', views.lichsu, name = "lichsu"),
    path('lichhenbs', views.appointment, name = "lichhenbs"),
    
    path('hosophongkham', views.hosophongkham, name = "hosophongkham"),
    path('quanlichinhanh', views.quanlichinhanh, name = "quanlichinhanh"),
    path('quanlidichvu', views.quanlidichvu, name = "quanlidichvu"),
    path('quanlinhanvien', views.quanlinhanvien, name = "quanlinhanvien"),

    path('quanlithongtinbenhnhan', views.quanlithongtinbenhnhan, name = "quanlithongtinbenhnhan"),
    path('hosobenhan/<int:record_id>/', views.hosobenhan_detail, name='hosobenhan_detail'),

    path('GioHang', views.Gio_Hang, name = "GioHang"),
    path('them_vao_gio_hang/<int:dich_vu_id>/', views.them_vao_gio_hang, name='them_vao_gio_hang'),
    path('xoa_khoi_gio_hang/<int:item_id>/', views.xoa_khoi_gio_hang, name='xoa_khoi_gio_hang'),
    # path('sua/<int:gio_hang_id>/', views.sua_so_luong, name='sua_so_luong'),
    path('sua_so_luong/<int:gio_hang_id>/', views.sua_so_luong, name='sua_so_luong'),
    path('manage/cart/<int:dich_vu_id>/add/', views.add_to_cart, name='add_to_cart'),
    path('thanh-toan/', views.thanh_toan, name='thanh_toan'),
    path('submit_dklichnghi', views.submit_dklichnghi, name = "submit_dklichnghi"),
    path('services/delete/<int:service_id>/', views.xoadichvu, name='xoadichvu'),
    path('suadichvu/<int:service_id>/', views.suadichvu, name='suadichvu'),
    path('quanlinhanvien/', views.manage_dentists, name='quanlinhanvien'),
    path('delete/<int:dentist_id>/', views.delete_dentist, name='delete_dentist'),
    path('edit/<int:dentist_id>/', views.edit_dentist, name='edit_dentist'),

]