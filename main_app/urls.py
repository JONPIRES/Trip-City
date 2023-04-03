from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('my-location/<str:query>/', views.my_location, name='my_location'),
]