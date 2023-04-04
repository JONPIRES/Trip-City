from django.db import models
from django.urls import reverse
from datetime import date 
from django.contrib.auth.models import User

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Trip Date')
    duration = models.IntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class Activities(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(Destination,on_delete=models.CASCADE)
    img = models.ImageField()
    