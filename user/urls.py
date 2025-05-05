"""
URL configuration for CDA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from user import views
from django.conf import settings    
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('reportcrime',views.reportcrimes),
    path('login',views.login),
    path('register',views.registers),
    path('contactus',views.contact_us),
    path('help',views.help),
    path('news',views.opennews),
    path('preview',views.preview),
    path('back',views.back),
    path('dashboard',views.dashboard),
    path('forgot',views.forgot),
    path('reset',views.reset),
    path('logout',views.logout),
    path('update',views.update),
    path('allnews',views.allnews),
    path('articles/',views.articles),
    path('articles2',views.articles2),
    path('urlfornews/',views.urlfornews),
    path('urlfornews2',views.urlfornews2),
]
