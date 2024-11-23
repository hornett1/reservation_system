from django.shortcuts import render
from .models import *

def user_list(request):
    users = User.objects.all()
    return render(request, 'reservation_app/index.html', {'users': users})

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'reservation_app/index.html', {'locations': locations})

def intro(request):
    return render(request, 'reservation_app/intro.html')

def location_detail(request, location_id):
    location = Location.objects.get(id=location_id)
    cars = location.car_set.all()
    if request.method == "POST":
        print(request.POST)
    return render(request, 'reservation_app/location_detail.html', {"location": location, "cars": cars})
