"""
    Class for defining API views
"""
from django.shortcuts import get_object_or_404, render
from ..models import Channel
import json

# Create your views here.


def assignment(request):
    """
        Handle the POST request from a PowerAutomate assignment listener
    """
    if request.POST:
        body = json.loads(request.body)
        # Get channel
        channel = get_object_or_404(Channel, pk=body['team']['uuid'])

    return render(request, 'index.html', {})
