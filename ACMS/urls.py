"""ACMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ACMS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage),
    path('Login', views.Loginpage),
    path('Help', views.Help),
    path('Services', views.Services),
    path('Contact', views.ContactUs),
    path('Getdetails', views.Getdetails),
    path('run-python-code/', views.run_python_code, name='run_python_code'),
    path('get-mac-address/', views.get_mac_address, name='get_mac_address'),
    path('get-uid/', views.get_uid, name='get_uid'),
]




