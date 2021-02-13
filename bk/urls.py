from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('pictures',views.pictures,name='pictures'),
  path('songs',views.songs,name='songs'),
  path('activities',views.activities,name='activities'),
  path('things',views.things,name='things'),
  path('memories',views.memories,name='memories'),

  path('pictures/upload',views.pictures_upload,name='pictures_upload'),
  path('songs/upload',views.songs_upload,name='songs_upload'),
  path('activities/upload',views.activities_upload,name='activities_upload'),
  path('things/upload',views.things_upload,name='things_upload'),
  path('memories/upload',views.memories_upload,name='memories_upload'),


  path('bk.css',views.css,name='css')
]
