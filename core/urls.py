"""
    Class for defining URL routes
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.pages.index, name='index'),
    path('api/assignment', views.api.assignment, name='assignment')
]