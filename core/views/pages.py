"""
    Class for defining page views
"""
from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Render the index page
    """
    return render(request, "index.html", {})


def calendar(request):
    """
    Render the calendar page
    """
    return render(request, "calendar.html", {})
