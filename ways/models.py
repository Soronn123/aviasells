from django.db import models
from django.forms import ValidationError

from airplanes.models import AirportModel, AircraftModel
from users.models import CustomUserModel

class RouteModel(models.Model):
    from_airport = models.ForeignKey(AirportModel, on_delete=models.CASCADE, related_name='departure_routes')
    to_airport = models.ForeignKey(AirportModel, on_delete=models.CASCADE, related_name='arrival_routes')
    distance_km = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.from_airport.name} → {self.to_airport.name}."

    class Meta:
        db_table = 'routes'


class FlightModel(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.ForeignKey(AirportModel, related_name='departures', on_delete=models.PROTECT)
    arrival = models.ForeignKey(AirportModel, related_name='arrivals', on_delete=models.PROTECT)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seats_available = models.PositiveIntegerField()
    created_by = models.ForeignKey(CustomUserModel, on_delete=models.PROTECT)

    def clean(self):
        if self.arrival_time <= self.departure_time:
            raise ValidationError("Arrival time must be after departure time")
    
    def __str__(self):
        return f"{self.flight_number}: {self.departure} → {self.arrival}"
