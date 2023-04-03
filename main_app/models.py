from django.db import models
from django.urls import reverse
from datetime import date 

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50)
    
