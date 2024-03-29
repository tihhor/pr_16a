from django.db import models

# Create your models here.
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.start),
    path('myapp', views.myapp, name='myapp')
]