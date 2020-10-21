"""
    Class for configuring the admin dashboard
"""
from django.contrib import admin
from .models import Channel, ChannelProxy, ChannelKey, Assignment


class AssignmentAdmin(admin.ModelAdmin):
    # Define field sections
    fieldsets = [
        ("Teams Data", {"fields": ["title", "subtitle", "url"]}),
        ("Date Information", {"fields": ["date_posted", "date_due"]}),
    ]
    list_display = ("title", "channel")


class ChannelAdmin(admin.ModelAdmin):

    # Define field sections
    fieldsets = [
        ("Teams Data", {"fields": ["uuid", "name", "description", "url"]}),
        ("App Data", {"fields": ["subject_name", "subject_code", "key"]}),
    ]

    # Define list display when viewing collectively
    list_display = ("name", "subject_code")


class TabularChannelAdmin(admin.TabularInline):
    model = ChannelProxy
    exclude = ["subject_name", "subject_code"]

    def has_change_permission(self, request, obj=None):
        return False
    
    verbose_name = "Channel Reference"
    verbose_name_plural = "Channel References"
    can_delete = False


class ChannelKeyAdmin(admin.ModelAdmin):
    inlines = [
        TabularChannelAdmin,
    ]


# Register your models here.

admin.site.register(ChannelKey, ChannelKeyAdmin)
admin.site.register(Channel, ChannelAdmin)

admin.site.register(Assignment, AssignmentAdmin)
