"""
    Class for defining URL routes
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main_list/',views.main_list, name="main_list"),
    path('main_grid/',views.main_grid, name="main_grid"),
    path('notifications/',views.notifications, name='notifications'),
    path('calendar/',views.calendar, name='calendar'),
    path('settings/',views.settings, name='settings'),
    path('add/',views.add, name='add'),
]