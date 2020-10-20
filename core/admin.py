"""
    Class for configuring the admin dashboard
"""
from django.contrib import admin
from .models import Channel, Assignment


class ChannelAdmin(admin.ModelAdmin):
    # Define field sections
    fieldsets = [
        ("Teams Data", {"fields": ["uuid", "name", "description", "url"]}),
        ("App Metadata", {"fields": ["subject_name", "subject_code", "connector_key"]}),
    ]

    # Define list display when viewing collectively
    list_display = ("name", "subject_code")

# Register your models here.
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Assignment)
