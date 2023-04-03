from django.shortcuts import render, redirect
from .services import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# \/\/this is for the functions so it requires you to be logged in
from django.contrib.auth.decorators import login_required
#\/\/ this is for the BCV so it requires you to be logged in
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
import os
import json

api_key = os.getenv('API_KEY')

print(f"this is my api_key: {api_key}")

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')
  

def signup(req):
  error_message = ''
  if req.method == "POST":
    form = UserCreationForm(req.POST)
    if form.is_valid():
      user=form.save()
      login(req, user)
      return redirect('index')
    else:
      error_message = 'invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(req, 'registration/signup.html', context)

# API functions \/\/\/

def my_location(request):
    query = request.GET.get('q')
    url = "https://travel-advisor.p.rapidapi.com/locations/v2/search"
    querystring = {"currency":"USD","units":"km","lang":"en_US"}
    payload = {
        "query": query,
        "updateToken": ""
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    data = json.loads(response.text)
    print(response.text)
    context = {'locations': data['data']}
    return render(request, 'api/search.html', context)