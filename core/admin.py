"""
    Class for configuring the admin dashboard
"""
from django.contrib import admin
from .models import Channel, Assignment

# Register your models here.
admin.site.register(Channel)
admin.site.register(Assignment)