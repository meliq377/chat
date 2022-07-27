from django.urls import path
from room.views import *


urlpatterns = [
    path('rooms/', rooms, name='rooms'),
    path('rooms/<str:slug>/', room, name='room'),


]