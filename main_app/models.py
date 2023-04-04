from django.db import models
from django.urls import reverse
from datetime import date 
from django.contrib.auth.models import User

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Trip Date',default=date.today)
    duration = models.IntegerField(default=1)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class Activities(models.Model):
    name = models.CharField(max_length=50)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    duration = models.IntegerField()
    date = models.DateField('Activity date',default=date.today)


    