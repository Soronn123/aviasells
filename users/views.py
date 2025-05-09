from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from ways.models import FlightModel
from cities.models import CountryModel, CityModel
from airplanes.models import AirportModel, AircraftModel

def index(request):
    return render(request, "index.html")


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def profile_view(request):
    if request.method == 'POST':
        try:
            user = request.user
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.middle_name = request.POST.get('middle_name', '')
            
            age = request.POST.get('age')
            if age:
                user.age = int(age) if age.isdigit() else None
            
            user.email = request.POST.get('email', '')
            user.save()
            messages.success(request, 'Profile updated successfully!')
        except Exception as e:
            messages.error(request, f'Error updating profile: {e}')
        
        return redirect('profile')

    flights = FlightModel.objects.filter(
        ticketmodel__user=request.user,
        ticketmodel__status__in=['booked', 'used']  
    ).distinct().select_related('departure', 'arrival')
    
    return render(request, 'users/profile.html', {
        'user': request.user,
        'flights': flights,
        'is_manager': request.user.is_manager
    })

@user_passes_test(lambda u: u.is_manager)
def manager_dashboard(request):
    context = {
        'countries': CountryModel.objects.all().order_by('name'),
        'cities': CityModel.objects.select_related('country').order_by('name'),
        'airports': AirportModel.objects.select_related('city', 'city__country').order_by('name'),
        'aircrafts': AircraftModel.objects.all().order_by('model_name'),
        'flights': FlightModel.objects.select_related(
            'departure', 'departure__city', 
            'arrival', 'arrival__city'
        ).order_by('-departure_time')[:20],
        'countries_count': CountryModel.objects.count(),
        'cities_count': CityModel.objects.count(),
        'airports_count': AirportModel.objects.count(),
        'aircrafts_count': AircraftModel.objects.count(),
        'flights_count': FlightModel.objects.count(),
    }
    return render(request, 'users/manager_dashboard.html', context)