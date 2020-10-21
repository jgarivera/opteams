"""
    Class for defining API views
"""
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound

from ..models import Channel
import json

# Create your views here.


@csrf_exempt
def assignment(request):
    """
    Handle the POST request from a PowerAutomate assignment listener
    """
    if request.method == "POST":
        body = json.loads(request.body)

        # Parse teams data object
        team_obj = body["team"]
        uuid = team_obj["uuid"]
        name = team_obj["name"]
        description = team_obj["description"]
        url = team_obj["url"]

        # Get or create channel if non-existent
        channel = Channel.objects.get_or_create(pk=uuid, defaults={
            "name": name,
            "description": description,
            "url": url
        })

        return JsonResponse({"channel": channel})

    return HttpResponseNotFound("Method not supported")
