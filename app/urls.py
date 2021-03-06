from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.show_dashboard, name='dash'),
    path('repo/<int:github_id>', views.show_repo, name="show_repo"),
]