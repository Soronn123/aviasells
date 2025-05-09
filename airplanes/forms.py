from django import forms
from .models import AirportModel, AircraftModel


class AirportForm(forms.ModelForm):
    class Meta:
        model = AirportModel
        fields = ['name', 'city']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
        }

class AircraftForm(forms.ModelForm):
    class Meta:
        model = AircraftModel
        fields = ['model_name', 'max_seats', 'max_km']
        widgets = {
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'max_seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_km': forms.NumberInput(attrs={'class': 'form-control'}),
        }