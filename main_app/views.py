from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Q
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

def world(request):
  act = Photo.objects.all()
  for photo in act:
        print("photos obj: ",photo.url)
  
  return render(request, 'world.html', {'act':act})

def search(request):
  query = request.GET.get('q', '')
  act = Photo.objects.filter(Q(title__icontains=query))
  return render(request, 'world.html', {'act':act})


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
  fields = ['name', 'date', 'days', 'notes']

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

class ActUpdate(LoginRequiredMixin,UpdateView):
    model=Activities
    fields=['name','duration', 'date', 'notes']

class ActDelete(LoginRequiredMixin,DeleteView):
    model=Activities
    success_url='/destination'

    # Post Functions


def post_index(request):
  post = Posts.objects.filter(user=request.user)
  return render(request, 'post/index.html', {
    'post': post
  })

@login_required
def post_detail(request, post_id):
    post = Posts.objects.get(id=post_id)
    user_id=request.user.id
    return render(request, 'post/detail.html', {
      'post': post,"user":user_id
  })

class PostCreate(LoginRequiredMixin,CreateView):
    model = Posts
    fields = ['description','rating', 'comment']

    def form_valid(self,form):
      # form.instance: is the user object based on the user model we're enheriting
      form.instance.user = self.request.user
      return super().form_valid(form)
      
class PostUpdate(LoginRequiredMixin,UpdateView):
    model=Posts
    fields=['description','comment', 'rating']

class PostDelete(LoginRequiredMixin,DeleteView):
    model=Posts
    success_url='/posts'

# Posts Photos \/\/

# For debugging purposes\/\/
# credentials = boto3.Session().get_credentials()
# print("printing creds ")
# print("AWS Access Key:", credentials.access_key)
# print("AWS Secret Key:", credentials.secret_key)

@login_required
def add_photo(req, post_id):
    photo_file = req.FILES.get('photo-file', None)
    
    if photo_file:
        # Initialize the S3 client
        s3 = boto3.client('s3')
        # Generate a unique key for the file using uuid (6 characters) this: photo_file.name[photo_file.name.rfind('.'):] is getting the "." and the extention
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        
        try:
            # Get the bucket name and base URL from environment variables
            bucket = os.getenv('S3_BUCKET')
            file_extension = photo_file.name.split('.')[-1].lower()
            if file_extension == 'jpeg' or file_extension == 'jpg':
                content_type = 'image/jpeg'
            elif file_extension == 'png':
                content_type = 'image/png'
            elif file_extension == 'gif':
                content_type = 'image/gif'
            else:
                content_type = 'application/octet-stream'
            s3.upload_fileobj(photo_file, bucket, key, ExtraArgs={'ContentType': content_type})
            
            # Construct the image URL using the base URL
            url = f"{os.getenv('S3_BASE_URL')}/{key}"
            # Get the additional fields (comment, title) from the form
            comment = req.POST.get('comment', '')
            title = req.POST.get('title', '')
            
            # Save the image details to the database
            Photo.objects.create(url=url, post_id=post_id, comment=comment, title=title)
        except Exception as e:
            # Handle any errors during upload
            print('An error occurred uploading file to S3')
            print(e)
    
    return redirect('post_detail', post_id=post_id)

class PostActUpdate(LoginRequiredMixin,UpdateView):
    model=Photo
    fields=['title','comment']

class PostActDelete(LoginRequiredMixin,DeleteView):
    model=Photo
    success_url='/posts'

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



