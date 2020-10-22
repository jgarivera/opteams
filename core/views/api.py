"""
    Class for defining API views
"""
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
from django.db import IntegrityError

from datetime import datetime
import json

from ..models import Channel, ChannelKey, Assignment


# Create your views here.


@csrf_exempt
def assignment(request):
    """
    Handle the POST request from a PowerAutomate assignment listener
    """
    if request.method == "POST":
        # Parse request body as JSON
        body = json.loads(request.body)

        # Attempt to retrieve key from request header
        try:
            key = request.headers["Key"]

            # Retrieve connector key from registry if available
            try:
                connector_key = ChannelKey.objects.get(secret=key)
            except ChannelKey.DoesNotExist:
                return HttpResponseBadRequest("Key not found")

            # Parse Teams data
            teams_obj = body["team"]

            # Get or create channel if it is non-existent and key is free
            try:
                channel = Channel.objects.get_or_create(
                    pk=teams_obj["uuid"],
                    defaults={
                        "name": teams_obj["name"],
                        "description": teams_obj["description"],
                        "url": teams_obj["url"],
                        "key": connector_key,
                    },
                )
            except IntegrityError:
                return HttpResponseBadRequest("Key is taken")

            # Parse assignment data
            assign_obj = body["assignment"]
            subtitle = assign_obj["subtitle"]

            # Attempt to parse date due
            try:
                date_due = datetime.strptime(f"{subtitle} 2020", "Due %b %d %Y")
            except ValueError:
                return HttpResponseBadRequest("Date parsing error")

            # Create assignment object
            assignment = Assignment(
                title=assign_obj["title"],
                subtitle=subtitle,
                url=assign_obj["url"],
                date_posted=assign_obj["datePosted"],
                date_due=date_due,
                channel=channel[0],
            )

            # Save assignment
            assignment.save()

            return JsonResponse({"success": True})
        except KeyError:
            return HttpResponseBadRequest("Key not found in registry")

    return HttpResponseBadRequest("Method not supported")
