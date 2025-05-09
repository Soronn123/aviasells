from django.contrib import admin

from .models import RouteModel, FlightModel

admin.site.register(RouteModel)
admin.site.register(FlightModel)
