from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # Destinations
  path('destination/', views.dest_index, name='index'),
  path('destination/<int:dest_id>/', views.dest_detail, name='dest_detail'),
  path('destination/create/', views.DestCreate.as_view(), name='destination_create'),
  path('destination/<int:pk>/update/', views.DestUpdate.as_view(), name='dest_update'),
  path('destination/<int:pk>/delete/', views.DestDelete.as_view(), name='dest_delete'),
  # Activities\/\/
  path('activities/<int:dest_id>/create/', views.add_activity, name='act_create'),
  path('activities/<int:pk>/delete/', views.ActDelete.as_view(), name='act_delete'),
  path('activities/<int:pk>/update/', views.ActUpdate.as_view(), name='act_update'),
  # Posts\/\/
  path('posts/', views.post_index, name='post_index'),
  path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
  path('posts/create/', views.PostCreate.as_view(), name='post_create'),
  path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
  path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
  # Photos
  path('photos/<int:post_id>/add_photo', views.add_photo, name='add_photo'),
  path('photos/<int:pk>/update/', views.PostActUpdate.as_view(), name='post_act_update'),
  path('photos/<int:pk>/delete/', views.PostActDelete.as_view(), name='post_act_delete'),
  # Users
  path('accounts/signup/', views.signup, name='signup'),

    
  # path('destinations/<int:pk>/update/', views.DestinationsUpdate.as_view(), name='destinations_update'),
  # path('destinations/<int:pk>/delete/', views.DestinationsDelete.as_view(), name='destinations_delete'),
  # path('destinations/<int:destinations_id>/add_accomodation/', views.add_accomodation, name='add_accomodation'),
  # path('destinations/<int:destinations_id>/add_photo/', views.add_photo, name='add_photo'),
  # path('destinations/<int:destinations_id>/assoc_activities/<int:activities_id>/', views.assoc_activities, name='assoc_activities'),
  # path('destinations/<int:destinations_id>/unassoc_activities/<int:activities_id>/', views.unassoc_activities, name='unassoc_activities'),
  # path('activities/', views.ActivitiesList.as_view(), name='activities_index'),
  # path('activities/<int:pk>/', views.ActivitiesDetail.as_view(), name='activities_detail'),
  
]