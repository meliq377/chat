from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required
def room(request):
    rooms = Room.objects.all()

    return render(request, 'rooms.html', {'rooms': rooms})
