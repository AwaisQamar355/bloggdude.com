from django.contrib import admin
from django.urls import path,include
from home import views
from django.urls import path
urlpatterns = [
    path('',views.home , name = 'home.html'),
    path('home.html',views.home , name = 'home.html'),
    path('Blog.html',views.Blog , name = 'Blog.html'),
    path('hosting.html',views.hosting , name = 'hosting.html'),
    path('Discount.html',views.Discount , name = 'Discount.html'),
    path('contact.html',views.contact , name = 'contact.html'),
    path('Gear.html',views.Gear , name = 'Gear.html'),
    path('login.html',views.loginUser , name = 'login.html'),
    path('logout.html',views.logoutUser, name = 'logout.html'),
]






