from django.db import models

from cities.models import CityModel


class AirportModel(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} ({self.city})"

    class Meta:
        db_table = 'airports'


class AircraftModel(models.Model):
    model_name = models.CharField(max_length=50)
    max_seats = models.PositiveIntegerField()
    max_km = models.PositiveIntegerField()

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'aircrafts'

