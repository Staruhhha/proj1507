from django.contrib import admin
from django.urls import path, include
from musicshop.views import *

urlpatterns = [
    path('test/', test)
]