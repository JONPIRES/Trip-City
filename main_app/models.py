from django.db import models
from django.urls import reverse
from datetime import date 
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Trip Date',default='')
    days = models.IntegerField(default=1)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(max_length=250, default='')

    def get_absolute_url(self):
        return reverse('dest_detail', kwargs={'dest_id': self.id})

class Activities(models.Model):
    name = models.CharField(max_length=50)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    duration = models.IntegerField(null=False, blank=False)
    date = models.DateField('Activity date',default=date.today)
    notes = models.TextField(max_length=250,default='')

    def get_absolute_url(self):
        return reverse('index')

RATING= (('1', '*'),('2','* *' ),('3', '* * *'),('4', '* * * *'),('5', '* * * * *'))


class Posts(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date = date.today
    description=models.CharField(max_length=50,default='', null=False, blank=False)
    comment = models.TextField(max_length=250)
    rating = models.CharField(
        max_length=1,
        choices = RATING,
        default=RATING[0][0])

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='',blank=True)
    comment = models.TextField(max_length=250, default="No comment")
    time = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now().time())

    def get_absolute_url(self):
        return reverse('post_index')
    
    class Meta:
        ordering = ['-time']


