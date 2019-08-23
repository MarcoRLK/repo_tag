from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
]