from django.shortcuts import render
from .models import *

def user_list(request):
    users = User.objects.all()
    return render(request, 'reservation_app/index.html', {'users': users})

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'reservation_app/index.html', {'locations': locations})
