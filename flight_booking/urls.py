from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('fetchflights/', views.fetchsearch),
    path('contact_us/', views.contactPage),
    path('fetchflights/<slug:Temparal_ID>/', views.addpassengerdetails, name="addpassengerdetails"),
    path('bookticket/<slug:Temparal_ID>/<slug:No_ticket>', views.handle_confirmation, name="handle_confirmation"),
    path('manageflight/', include('Airline.urls')),
    path('auth/', include('user.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
