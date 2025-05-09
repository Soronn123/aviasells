from django.db import models
from django.contrib.auth.models import AbstractUser

from cities.models import CountryModel

class CustomUserModel(AbstractUser):
    """
    Custioom User Model
    """
    middle_name = models.CharField(max_length=30, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, null=True, blank=True)

    class Role(models.TextChoices):
        USER = 'user', 'User'
        MANAGER = 'manager', 'Manager'
        ADMIN = 'admin', 'Admin'
    
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )
    
    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER
    
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser
    
    class Meta:
        db_table = 'users'
    