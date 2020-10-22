"""
    Class for defining page views
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from ..models import Channel, Assignment
import stream

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

    # Retrieve all assignments
    assignments = Assignment.objects.all()

    context = {"assignments": assignments}
    return render(request, "calendar.html", context)


@login_required
def notifications(request):
    """
        Render notifications page
    """
    # Create stream client
    client = stream.connect(settings.STREAM_IO_KEY, settings.STREAM_IO_SECRET)

    # Retrieve notifications
    notifications = client.feed("notification", request.user.username)
    activities = notifications.get(limit=10)["results"]

    context = {"activities": activities}
    return render(request, "index.html", context)
