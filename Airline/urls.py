from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings 
from . import views

urlpatterns = [
        path('<slug:Airline_id>/', views.manageflight),
        path('update/<slug:Flight_id>/', views.updateflight),
        path('add/<slug:Airline_id>/', views.createflight),
        path('add/success/<slug:Airline_id>/', views.sucessflight),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
