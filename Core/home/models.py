from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    pricde = models.IntegerField()
    description = models.TextField()
    quntity = models.IntegerField(default=0)

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    car_id = models.IntegerField() 
    speed = models.IntegerField(default=0)

    def __str__(self):
        return self.car_name
    
