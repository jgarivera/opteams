"""
    Class for defining page views
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings as conf_settings

from ..models import Channel, Assignment
import stream

# Create your views here.


@login_required
def index(request):
    """
    Render the index page
    """

    # Retrieve all assignments from user's channel subscriptions
    profile = request.user.userprofile
    subscribed_channels = profile.subscriptions.all()
    assignments = Assignment.objects.in_date_due_order(channel__in=subscribed_channels)

    context = {"assignments": assignments}
    return render(request, "index_list.html", context)


@login_required
def main_grid(request):
    context = {}
    return render(request, "index_grid.html", context)


@login_required
def calendar(request):
    """
    Render calendar page
    """

    # Retrieve all assignments from user's channel subscriptions
    profile = request.user.userprofile
    subscribed_channels = profile.subscriptions.all()
    assignments = Assignment.objects.in_date_due_order(channel__in=subscribed_channels)

    context = {"assignments": assignments}
    return render(request, "calendar.html", context)


@login_required
def notifications(request):
    """
    Render notifications page
    """

    # Create stream client
    client = stream.connect(conf_settings.STREAM_IO_KEY, conf_settings.STREAM_IO_SECRET)

    # Retrieve notifications
    notifications = client.feed("notification", request.user.username)
    activities = notifications.get(limit=10)["results"][0]["activities"]

    context = {"activities": activities}
    return render(request, "notifications.html", context)


@login_required
def settings(request):
    """
    Render settings page
    """
    context = {}
    return render(request, "settings.html", context)