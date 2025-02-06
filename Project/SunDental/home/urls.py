from django.contrib import admin
from django.urls import include, path
from.import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('service/', views.service_view, name='service'),
    path('register/', views.register, name = 'register'),
    path('login/', views.register, name = 'login'),
    path('news/', views.news_view, name='news'),
    path('learning/', views.learning_view, name='learning'),
    path('contact/', views.contact_view, name='contact'),
    path('event/', views.event_view, name='event'),
]