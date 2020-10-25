"""
    Class for defining URL routes
"""
from django.urls import path

from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('main_list/',TemplateView.as_view(template_name='main_list.html'), name="main_list"),
    path('main_grid/',TemplateView.as_view(template_name='main_grid.html'), name="main_grid"),
    path('notifications/',TemplateView.as_view(template_name='notifications.html'), name='notifications'),
    path('calendar/',TemplateView.as_view(template_name='calendar.html'), name='calendar'),
    path('task_list/',TemplateView.as_view(template_name='task_list.html'), name='task_list'),
    path('settings/',TemplateView.as_view(template_name='settings.html'), name='settings'),
    path('add/',TemplateView.as_view(template_name='add.html'), name='add'),
]