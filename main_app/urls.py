from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('destinations/', views.dest_index, name='index'),
  path('destination/<int:dest_id>/', views.dest_detail, name='dest_detail'),
  path('destination/create/', views.DestCreate.as_view(), name='destination_create'),
  path('destination/<int:pk>/update/', views.DestUpdate.as_view(), name='dest_update'),
  path('destination/<int:pk>/delete/', views.DestDelete.as_view(), name='dest_delete'),
  path('destination/<int:dest_id>/add_act/', views.add_activity, name='add_activity'),
  path('accounts/signup/', views.signup, name='signup'),
  
    
  # path('destinations/<int:pk>/update/', views.DestinationsUpdate.as_view(), name='destinations_update'),
  # path('destinations/<int:pk>/delete/', views.DestinationsDelete.as_view(), name='destinations_delete'),
  # path('destinations/<int:destinations_id>/add_accomodation/', views.add_accomodation, name='add_accomodation'),
  # path('destinations/<int:destinations_id>/add_photo/', views.add_photo, name='add_photo'),
  # path('destinations/<int:destinations_id>/assoc_activities/<int:activities_id>/', views.assoc_activities, name='assoc_activities'),
  # path('destinations/<int:destinations_id>/unassoc_activities/<int:activities_id>/', views.unassoc_activities, name='unassoc_activities'),
  # path('activities/', views.ActivitiesList.as_view(), name='activities_index'),
  # path('activities/<int:pk>/', views.ActivitiesDetail.as_view(), name='activities_detail'),
  # path('activities/create/', views.ActivitiesCreate.as_view(), name='activities_create'),
  # path('activities/<int:pk>/update/', views.ActivitiesUpdate.as_view(), name='activities_update'),
  # path('activities/<int:pk>/delete/', views.ActivitiesDelete.as_view(), name='activities_delete'),
  
]