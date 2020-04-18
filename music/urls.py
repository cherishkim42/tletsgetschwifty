from django.contrib import admin
from django.urls import include, path 

from . import views

urlpatterns = [
    # path('music', include(music.urls)),
    path('', views.index, name='index'),
    # path('<str:album_name>/', views.one_album, name='one_album'),
]