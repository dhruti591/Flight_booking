from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('register/', views.auth_register),
    path('login/', views.auth_login),
    path('logout/', views.auth_logout),
    path('profile/', views.auth_profile),
    path('profile/<slug:username>', views.change_profile),
]
