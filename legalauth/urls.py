from django.contrib import admin
from django.urls import path,include
from django.conf import settings    
from django.conf.urls.static import static
from legalauth import views

urlpatterns = [   
    path('',views.ladashboard),
    path('login',views.login),
    path('ladashboard',views.ladashboard),
    path('details',views.details),
    path('profile',views.profile),
    path('statusupdate',views.statusupdate),
    path('update',views.update),
    path('logout',views.logout),
    path('fake',views.fakecom),
]
