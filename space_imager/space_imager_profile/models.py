from django.db import models


class Space_Image(models.Model):
    """Model for a Space Photo."""
    copyright = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True)
    explanation = models.TextField(max_length=2000)
    hdurl = models.CharField(max_length=180)
    media_type = models.TextField(max_length=50)
    service_version = models.CharField(max_length=2)
    title = models.TextField(max_length=50)
    url = models.CharField(max_length=180)
