from django.forms import ValidationError
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import CountryForm, CityForm

@user_passes_test(lambda u: u.is_manager)
def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Country added successfully')
                return redirect('manager_dashboard')
            except ValidationError as e:
                messages.error(request, e.message)
    else:
        form = CountryForm()
    return render(request, 'cities/add_country.html', {'form': form})

@user_passes_test(lambda u: u.is_manager)
def add_city(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'City added successfully')
                return redirect('manager_dashboard')
            except ValidationError as e:
                messages.error(request, e.message)
    else:
        form = CityForm()
    return render(request, 'cities/add_city.html', {'form': form})