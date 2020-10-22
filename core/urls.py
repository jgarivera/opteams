"""
    Class for defining URL routes
"""
from django.urls import path

from . import views

urlpatterns = [
    # Page routes
    path("", views.pages.index, name="index"),
    path("calendar", views.pages.calendar, name="calendar"),
    path("notifications", views.pages.notifications, name="notifications"),
    
    # API routes
    path("api/assignment", views.api.assignment, name="assignment"),
]