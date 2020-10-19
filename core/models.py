"""
    Class for defining database model schemas
"""
from django.db import models

# Create your models here.


class Assignment(models.Model):
    """
        Assignment model class
    """
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_posted = models.DateTimeField('date posted')
    date_due = models.DateTimeField('date due')

    def __str__(self):
        return self.title


class Channel(models.Model):
    """
        Channel model class
            * uuid - universal unique identifier; provided ID by Teams
    """
    uuid = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
