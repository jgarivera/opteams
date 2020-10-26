"""
    Class for defining database model schemas
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from .managers import AssignmentManager
import stream

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
            has_channel = self.channel is not None
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
    """

    uuid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    key = models.OneToOneField(ChannelKey, on_delete=models.CASCADE)

    def get_short_name(self):
        n = self.subject_name.split()
        found = 0
        for i in n:
            f = i[0]
            if f.isalpha() and f.isupper() and found == 0:
                found = 1
                first = i[0]
            elif f.isalpha() and f.isupper() and found == 1:
                found = 2
                second = i[0]
            if found == 2:
                return first + second

    def get_assignment_count(self):
        return Assignment.objects.filter(channel=self.uuid).count()

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
    objects = AssignmentManager()

    def is_past_due(self):
        now = timezone.now()
        return now >= self.date_due

    def __str__(self):
        return self.title


@receiver(post_save, sender=Assignment)
def notify_assignment(sender, instance, created, **kwargs):
    if created:
        # Create stream client
        client = stream.connect(settings.STREAM_IO_KEY, settings.STREAM_IO_SECRET)

        # Retrieve all profiles
        channel = instance.channel
        profiles = channel.userprofile_set.all()

        # Send notification to every subscriber
        for p in profiles:
            username = p.user.username
            feed = client.feed("notification", username)
            feed.add_activity(
                {
                    "actor": channel.name,
                    "verb": "add",
                    "object": f"{instance.title};{instance.subtitle}",
                    "foreign_id": instance.id,
                }
            )


class UserProfile(models.Model):
    """
    User profile class
        * user - user object reference
        * subscriptions - list of channels user is subscribed to
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField(Channel)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
