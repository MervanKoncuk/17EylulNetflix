from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('movies/<str:slug>/<str:id>', movies, name='movies'),
    path('search/', search, name='search'),
    path('video/<str:filmId>', video, name='video')
]