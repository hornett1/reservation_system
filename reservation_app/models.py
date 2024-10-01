from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=150)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=250)
    year = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    damage = models.TextField()
    mileage = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

class User(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=50)
    rating = models.FloatField(default=0, )
    reputation = models.FloatField(default=0)
    cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.name


class Company(User):
    clients_per_month = models.IntegerField(default=0)




