from django.forms import ValidationError
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import AirportForm, AircraftForm

@user_passes_test(lambda u: u.is_manager)
def add_airport(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Airport added successfully')
                return redirect('manager_dashboard')
            except ValidationError as e:
                messages.error(request, e.message)
    else:
        form = AirportForm()
    return render(request, 'airplanes/add_airport.html', {'form': form})


@user_passes_test(lambda u: u.is_manager)
def add_aircraft(request):
    if request.method == 'POST':
        form = AircraftForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Aircraft added successfully')
                return redirect('manager_dashboard')
            except ValidationError as e:
                messages.error(request, e.message)
    else:
        form = AircraftForm()
    return render(request, 'airplanes/add_aircraft.html', {'form': form})