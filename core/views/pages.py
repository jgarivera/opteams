"""
    Class for defining page views
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    """
    Render the index page
    """
    return render(request, "index.html", {})


@login_required
def calendar(request):
    """
    Render the calendar page
    """
    return render(request, "calendar.html", {})
