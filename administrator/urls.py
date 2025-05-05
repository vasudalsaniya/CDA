from django.contrib import admin
from django.urls import path,include
from django.conf import settings    
from django.conf.urls.static import static
from administrator import views

urlpatterns = [
    path('',views.login),
    path('alogin',views.login),
    path('dashboard',views.dashboard),
    path('addauth',views.addauth),
    path('viewauth',views.seeauth),
    path('auth',views.allauth),
    path('viewcom',views.viewcom),
    path('update',views.update),
    path('afake',views.fakecom),
    path('addnews',views.addnews),
]
