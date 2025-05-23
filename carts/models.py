from django.db import models
from users.models import CustomUserModel
from ways.models import FlightModel


class Cart(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    flight = models.ForeignKey(FlightModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.flight.flight_number}"