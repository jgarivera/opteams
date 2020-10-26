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
    Render the index page - main_list
    """

    # Retrieve all assignments from user's channel subscriptions
    profile = request.user.userprofile
    subscribed_channels = profile.subscriptions.all()
    assignments = Assignment.objects.in_date_due_order(channel__in=subscribed_channels)

    context = {"assignments": assignments}
    return render(request, "index_list.html", context)


@login_required
def main_grid(request):
    # Retrieve all assignments from user's channel subscriptions
    profile = request.user.userprofile
    subscribed_channels = profile.subscriptions.all()

    channel_assignment_map = {}

    for c in subscribed_channels:
        assignments = Assignment.objects.in_date_due_order(channel=c)
        channel_assignment_map[c] = assignments

    channel_assignments = []
    for key, value in channel_assignment_map.items():
        ca = []
        # Append channel object
        ca.append(key)
        # Append assignments
        for v in value:
            ca.append(v)
        channel_assignments.append(ca)

    print(channel_assignments)
    context = {"channel_assignments": channel_assignments}
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