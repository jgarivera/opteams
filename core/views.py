"""
    Class for defining views
"""
from django.shortcuts import render

# Create your views here.
def index(request):
    """
        Render the index page
    """
    return render(request, 'index.html')

def main_list(request):
    return render(request, 'main_list.html')

def main_grid(request):
    return render(request, 'main_grid.html')

def notifications(request):
    return render(request, 'notifications.html')

def calendar(request):
    return render(request, 'calendar.html')

def task_list(request):
    return render(request, 'task_list.html')

def settings(request):
    return render(request, 'settings.html')

def add(request):
    return render(request, 'add.html')