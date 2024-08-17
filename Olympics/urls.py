"""
URL configuration for Olympics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from apps.medals.api.viewsets import CountryViewsets, SportViewsets, MedalViewsets
from rest_framework import routers

# Configuração das rotas
route = routers.DefaultRouter() 
route.register('Country', CountryViewsets, basename='Country')
route.register('Sport', SportViewsets, basename='Sport')
route.register('Medal', MedalViewsets, basename='Medal')

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", include(route.urls), name="medals-livros"),  
]


