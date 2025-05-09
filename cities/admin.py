from django.contrib import admin

from .models import CityModel, CountryModel

admin.site.register(CityModel)
admin.site.register(CountryModel)
