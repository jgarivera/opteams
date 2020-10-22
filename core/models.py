"""
    Class for defining database model schemas
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class ChannelKey(models.Model):
    """
    Channel key model class
        * secret - md5 string hash for API authentication
        * alias - nickname for this key
    """

    secret = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)

    def __str__(self):
        return self.alias

    def is_taken(self):
        has_channel = False
        try:
            has_channel = (self.channel is not None)
        except Channel.DoesNotExist:
            pass
        return has_channel



class Channel(models.Model):
    """
    Channel model class
        * uuid - universal unique identifier; provided by Teams
        * name - channel name; provided by Teams
        * description - channel description; provided by Teams
        * url - channel link; provided by Teams

        * subject_name - subject name
        * subject_code - subject code
        * key - connector key object
        * subscribers - list of subscribed users to this channel
    """

    uuid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    key = models.OneToOneField(ChannelKey, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class ChannelProxy(Channel):
    class Meta:
        proxy = True


class Assignment(models.Model):
    """
    Assignment model class
        * title - assignment name; provided by Teams
        * subtitle - assigment due text; provided by Teams
        * url - assignment link; provided by Teams
        * date_posted - date when message was posted; provided by Teams

        * date_due - date when assignment is due
        * channel - channel in which this assignment belongs to
    """

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_posted = models.DateTimeField("date posted")
    date_due = models.DateTimeField("date due")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def is_past_due(self):
        now = timezone.now()
        return now >= self.date_due

    def __str__(self):
        return self.title
