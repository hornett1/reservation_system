from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=250)
    year = models.IntegerField()
    power = models.IntegerField()
    damage = models.TextField()
    mileage = models.IntegerField()

class Location(models.model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=50)
    rating = models.FloatField()
    reputation = models.FloatField()
    rented_cars = models.ForeignKey(Car, on_delete=models.CASCADE)

class Company(User):
    clients_per_month = models.IntegerField()




