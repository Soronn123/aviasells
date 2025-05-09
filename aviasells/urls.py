"""
URL configuration for aviasells project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users import views as userViews 
from ways import views as waysViews
from cities import views as cititesViews
from airplanes import views as airplanesViews
from carts import views as cartsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", userViews.index, name="home"),

    path('register/', userViews.register_view, name='register'),
    path('login/', userViews.login_view, name='login'),
    path('logout/', userViews.logout_view, name='logout'),
    path('profile/', userViews.profile_view, name='profile'),

    path('manager/', userViews.manager_dashboard, name='manager_dashboard'),

    path('manager/country/add/', cititesViews.add_country, name='add_country'),
    path('manager/city/add/', cititesViews.add_city, name='add_city'),
    path('manager/airport/add/', airplanesViews.add_airport, name='add_airport'),
    path('manager/aircraft/add/', airplanesViews.add_aircraft, name='add_aircraft'),
    path('manager/flight/add/', waysViews.add_flight, name='add_flight'),

    path('flights/', waysViews.flights_list, name='flights_list'),
    path('flights/my/', waysViews.my_flights, name='my_flights'),
    path('flights/map/', waysViews.flight_map, name='flight_map'),

    path('cart/add/<int:flight_id>/', cartsViews.add_to_cart, name='add_to_cart'),
    path('cart/', cartsViews.view_cart, name='view_cart'),
    path('cart/remove/<int:item_id>/', cartsViews.remove_from_cart, name='remove_from_cart'),
]
