from django.contrib import admin
from Airline.models import Airline, Airline_manager

admin.site.register(Airline_manager)
admin.site.register(Airline)
