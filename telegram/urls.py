from django.contrib import admin
from django.urls import path , include
from telegram.views import login_user , register

urlpatterns = [
    path('' , login_user , name="home"),
    path("nima" , register , name="register"),
]

