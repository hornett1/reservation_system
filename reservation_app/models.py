from django.db import models

class Location(models.Model):
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=150)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.region}, {self.country}"

class User(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=50)
    rating = models.FloatField(default=0, )
    reputation = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=250)
    year = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    car_engine_volume = models.FloatField(default=0)
    damage = models.TextField()
    mileage = models.IntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

class Booking(models.Model):
    start_date = models.DateTimeField()
    duration = models.DurationField()
    tenant = models.ForeignKey(User, related_name="tenant", on_delete=models.DO_NOTHING)
    renter = models.ForeignKey(User, related_name="renter", on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    


