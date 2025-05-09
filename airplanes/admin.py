from django.contrib import admin

from .models import AirportModel, AircraftModel

admin.site.register(AirportModel)
admin.site.register(AircraftModel)