from django import forms
from .models import CountryModel, CityModel

class CountryForm(forms.ModelForm):
    class Meta:
        model = CountryModel
        fields = ['name', 'is_country']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter country name'
            }),
            'is_country': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            }),
        }

class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = ['name', 'country']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter city name'
            }),
            'country': forms.Select(attrs={
                'class': 'w-full p-2 border rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
            }),
        }
