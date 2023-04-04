from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('my_location/', views.my_location, name='my_location'),
  
  path('trip/', views.trip_index, name='index'),
  path('trip/<int:trip_id>/', views.Trip_detail, name='detail'),
  path('trip/create/', views.TripCreate.as_view(), name='trip_create'),
  path('trip/<int:pk>/update/', views.TripUpdate.as_view(), name='trip_update'),
  path('trip/<int:pk>/delete/', views.TripDelete.as_view(), name='trip_delete'),
  path('trip/<int:trip_id>/add_accomodation/', views.add_accomodation, name='add_accomodation'),
  path('trip/<int:trip_id>/add_photo/', views.add_photo, name='add_photo'),
  path('trip/<int:trip_id>/assoc_event/<int:event_id>/', views.assoc_event, name='assoc_event'),
  path('trip/<int:trip_id>/unassoc_event/<int:event_id>/', views.unassoc_event, name='unassoc_event'),
  path('event/', views.EventList.as_view(), name='event_index'),
  path('event/<int:pk>/', views.EventDetail.as_view(), name='event_detail'),
  path('event/create/', views.EventCreate.as_view(), name='event_create'),
  path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
  path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  
]