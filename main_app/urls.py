from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('destination/<int:dest_id>/', views.Dest_detail, name='dest_detail'),
  
    
  # path('destination/', views.destination_index, name='index'),
  # path('destination/create/', views.DestinationCreate.as_view(), name='destination_create'),
  # path('destination/<int:pk>/update/', views.DestinationUpdate.as_view(), name='destination_update'),
  # path('destination/<int:pk>/delete/', views.DestinationDelete.as_view(), name='destination_delete'),
  # path('destination/<int:destination_id>/add_accomodation/', views.add_accomodation, name='add_accomodation'),
  # path('destination/<int:destination_id>/add_photo/', views.add_photo, name='add_photo'),
  # path('destination/<int:destination_id>/assoc_activities/<int:activities_id>/', views.assoc_activities, name='assoc_activities'),
  # path('destination/<int:destination_id>/unassoc_activities/<int:activities_id>/', views.unassoc_activities, name='unassoc_activities'),
  # path('activities/', views.ActivitiesList.as_view(), name='activities_index'),
  # path('activities/<int:pk>/', views.ActivitiesDetail.as_view(), name='activities_detail'),
  # path('activities/create/', views.ActivitiesCreate.as_view(), name='activities_create'),
  # path('activities/<int:pk>/update/', views.ActivitiesUpdate.as_view(), name='activities_update'),
  # path('activities/<int:pk>/delete/', views.ActivitiesDelete.as_view(), name='activities_delete'),
  
]