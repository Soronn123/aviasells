from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ways.models import FlightModel
from carts.models import Cart, CartItem

def add_to_cart(request, flight_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to add flights to your cart")
        return redirect('login')
    
    flight = get_object_or_404(FlightModel, id=flight_id)
    
    # Получаем или создаем корзину
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Добавляем рейс в корзину
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        flight=flight,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Сохраняем ID добавленного рейса в сессии
    if 'added_flights' not in request.session:
        request.session['added_flights'] = []
    
    if flight.id not in request.session['added_flights']:
        request.session['added_flights'].append(flight.id)
        request.session.modified = True
    
    messages.success(request, f"Flight {flight.flight_number} has been added to your cart")
    return redirect('flights_list')

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    cart = get_object_or_404(Cart, user=request.user)
    for item in cart.items.all():
        item.total_price = item.flight.price * item.quantity

    return render(request, 'carts/view_cart.html', {'cart': cart})

def remove_from_cart(request, item_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please login to manage your cart")
        return redirect('login')
    
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    flight_number = cart_item.flight.flight_number
    cart_item.delete()
    
    # Обновляем сессию
    if 'added_flights' in request.session:
        if cart_item.flight.id in request.session['added_flights']:
            request.session['added_flights'].remove(cart_item.flight.id)
            request.session.modified = True
    
    messages.success(request, f"Flight {flight_number} has been removed from your cart")
    return redirect('view_cart')