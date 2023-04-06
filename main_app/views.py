from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from .forms import ActivitiesForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# \/\/this is for the functions so it requires you to be logged in
from django.contrib.auth.decorators import login_required
#\/\/ this is for the BCV so it requires you to be logged in
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
import os



# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def dest_index(request):
  dest = Destination.objects.filter(user=request.user)
  return render(request, 'destinations/index.html', {
    'dest': dest
  })

# Destinations Functions\/\/\/

class DestCreate(LoginRequiredMixin,CreateView):
  model = Destination
  fields = ['name', 'date', 'days', 'notes']

  def form_valid(self,form):
    # form.instance: is the user object based on the user model we're enheriting
    form.instance.user = self.request.user
    return super().form_valid(form)

@login_required  
def dest_detail(request, dest_id):
    dest = Destination.objects.get(id=dest_id)
    act_form = ActivitiesForm()
    return render(request, 'destinations/detail.html', {
      'dest': dest, 'act_form': act_form
  })
  
class DestUpdate(LoginRequiredMixin,UpdateView):
  model = Destination
  fields = ['name', 'date', 'days']

class DestDelete(LoginRequiredMixin,DeleteView):
  model = Destination
  success_url = '/destination'

# Activities Form\/\/\/

@login_required
def add_activity(request, dest_id):
  form = ActivitiesForm(request.POST)

  if form.is_valid():
    new_act = form.save(commit=False)
    new_act.destination_id = dest_id
    new_act.save()
    return redirect('dest_detail', dest_id=dest_id)

class ActUpdate(UpdateView):
    model=Activities
    fields=['name','duration', 'date', 'notes']

class ActDelete(DeleteView):
    model=Activities
    success_url='/destination'

    # Post Functions

def post_index(request):
  post = Posts.objects.all()
  return render(request, 'post/index.html', {
    'post': post
  })

@login_required  
def post_detail(request, post_id):
    post = Posts.objects.get(id=post_id)
    return render(request, 'post/detail.html', {
      'post': post
  })

class PostCreate(LoginRequiredMixin,CreateView):
    model = Posts
    fields = ['description','rating', 'comment']

    def form_valid(self,form):
      # form.instance: is the user object based on the user model we're enheriting
      form.instance.user = self.request.user
      return super().form_valid(form)
      
class PostUpdate(UpdateView):
    model=Activities
    fields=['description','comment', 'rating']

class PostDelete(DeleteView):
    model=Activities
    success_url='/posts'

# Posts Photos \/\/

def add_photo(req,post_id):
  photo_file = req.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    #uuid generates a hex of 32 charactrers but we drop that to 6 characters with the [:6]  / the rfind wants to find the '.' in the name and the basically get the '. and the rest whick would be the file type (.jpg)
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.getenv('S3_BUCKET')
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.getenv('S3_BUCKET')}{bucket}/{key}"
      comment = req.POST.get('comment', '')
      Photo.objects.create(url=url, post_id=post_id, comment=comment)
    except Exception as e:
      print('an error occured uploading file to s3')
      print(e)
  return redirect('post_detail', post_id=post_id)



  # User Functions \/\/

def signup(req):
  error_message = ''
  if req.method == "POST":
    form = UserCreationForm(req.POST)
    if form.is_valid():
      user=form.save()
      login(req, user)
      return redirect('home')
    else:
      error_message = 'invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(req, 'registration/signup.html', context)



