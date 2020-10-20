"""
    Class for defining URL routes
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.pages.index, name='index'),
]