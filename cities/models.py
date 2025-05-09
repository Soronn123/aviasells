from django.db import models


class CountryModel(models.Model):
    """
    Country model
    """
    name = models.CharField(max_length=100, unique=True)
    is_country = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'countries'

class CityModel(models.Model):
    """
    City model
    """
    name = models.CharField(max_length=100)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.country.name}"

    class Meta:
        db_table = 'cities'


        