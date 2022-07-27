from django.urls import path
from chat.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),

]
