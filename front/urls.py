"""python URL Configuration

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
from rest_framework import routers
from .api import ProjectviewSet
from django.contrib import admin
from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login, name="login"),
    path('jokes/',views.jokes, name="Get_Jokes"),
    path('my_jokes/<str:email>',views.myjokes, name="My_Jokes"),
    path('getjokes/<str:uuid>',views.getjokes, name="GET"),
    path('addjoke/<str:ur>/<str:email>',views.addjoke, name="GET"),
    path('list_jokes/',views.listjokes, name="listjokes"),
    path('list_joke/<str:uuid>',views.listjoke, name="listJoke"),
    path('update_joke/<str:ids>',views.updatejoke, name="updateJoke"),
    path('delete_joke/<str:ids>',views.deletejoke, name="deleteJoke"),
    path('create_joke/',views.createjoke, name="createJoke"),
    
    
    
    
]