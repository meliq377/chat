from django.urls import path
from room.views import *


urlpatterns = [
    path('rooms/', room, name='rooms'),


]