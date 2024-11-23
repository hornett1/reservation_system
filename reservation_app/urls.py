from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('users/', user_list, name="users-list"),
    path('locations/', location_list, name="locations-list"),
    path('', intro, name="main"),
    path('location_detail/<int:location_id>', location_detail, name="location-detail")
]
