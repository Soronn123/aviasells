from django import forms
from .models import FlightModel

class FlightForm(forms.ModelForm):
    class Meta:
        model = FlightModel
        fields = ['flight_number', 'departure', 'arrival', 'departure_time', 
                 'arrival_time', 'price', 'seats_available']
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'flight_number': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
            'seats_available': forms.NumberInput(attrs={'class': 'form-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'w-full p-2 border rounded'})