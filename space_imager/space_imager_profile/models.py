"""Model for a Space Photo taken from NASA."""

from django.db import models
from space_imager_profile.nasa_api_interface import NASASpacePhotoAPICallInterface

class Space_Photo_From_NASA(models.Model, NASASpacePhotoAPICallInterface): 

    objects = models.Manager

    date = models.DateTimeField(auto_now=True)
    explanation = models.TextField(max_length=2000, null=True)
    hdurl = models.CharField(max_length=180, null=True)
    media_type = models.TextField(max_length=50, null=True)
    service_version = models.CharField(max_length=2, null=True)
    title = models.TextField(max_length=50)
    url = models.CharField(max_length=180, null=True)

    def __str__(self):
        return self.title
