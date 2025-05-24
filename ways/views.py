from django.utils import timezone
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import FlightModel
from .forms import FlightForm
from cities.models import CityModel
from django.contrib import messages
from django.db.models import Q

def flights_list(request):
    flights = FlightModel.objects.all().select_related('departure', 'arrival', 'departure__city', 'arrival__city')
    return render(request, 'ways/list.html', {
        'flights': flights,
        'is_manager': request.user.is_manager
    })

@login_required
@user_passes_test(lambda u: u.is_manager)
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.created_by = request.user
            
            try:
                flight.full_clean()
                flight.save()
                return redirect('flights_list')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = FlightForm()
    
    return render(request, 'ways/add.html', {'form': form})



@login_required
def my_flights(request):
    flights = FlightModel.objects.filter(
        cartitem__cart__user=request.user
    ).distinct().select_related(
        'departure',
        'departure__city',
        'departure__city__country',
        'arrival',
        'arrival__city',
        'arrival__city__country'
    ).prefetch_related('cartitem_set')
    
    return render(request, 'ways/my_flights.html', {
        'flights': flights,
        'is_manager': request.user.is_manager,
        'now': timezone.now()
    })


def flight_map(request):
    # Получаем только рейсы, где оба города имеют координаты
    flights = FlightModel.objects.filter(
        departure__city__latitude__isnull=False,
        departure__city__longitude__isnull=False,
        arrival__city__latitude__isnull=False,
        arrival__city__longitude__isnull=False
    ).select_related(
        'departure__city',
        'arrival__city'
    )[:10]  # Ограничиваем количество для примера
    
    if not flights.exists():
        messages.warning(request, "No flights found where both departure and arrival cities have coordinates")
    return render(request, 'ways/flight_map.html', {
        'flights': flights,
        'City': CityModel  # Передаем модель для отладочной информации
    })