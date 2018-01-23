"""Model for a Space Photo taken from NASA."""

from django.db import models
from django.dispatch import receiver
from space_imager_profile.space_photo_from_api import NASA_Space_Photo_DTO
from django.contrib.auth.models import User

import requests

'''
class Space_Photo_From_API_Model(models.Model):
    """Model for a Space Photo."""
    copyright = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True)
    explanation = models.TextField(max_length=2000)
    hdurl = models.CharField(max_length=180)
    media_type = models.TextField(max_length=50)
    service_version = models.CharField(max_length=2)
    title = models.TextField(max_length=50)
    url = models.CharField(max_length=180)

    def __str__(self):
        """Print function returns title of photo."""
        return self.title

@receiver(models.signals.post_save, sender=User)
def create_space_photo_from_api_object(sender, **kwargs):
    """Create the profile when a user is created."""
    if kwargs['created']:
        space_photo_from_api_object = Space_Photo_From_API_Model(user=kwargs['instance'])
        import pdb; pdb.set_trace()
        space_photo_from_api_object.save()
'''


class SpacePhotoManager(models.Manager):
    def create_space_photo(self):
        #https://api.nasa.gov/planetary/apod?api_key=sgQen3xfYyYvOzwtIn1QKeCe5SmHiFxLjdIVv6lz
        nasa_apod_url = 'https://api.nasa.gov/planetary/apod?api_key='
        nasa_api_key = 'sgQen3xfYyYvOzwtIn1QKeCe5SmHiFxLjdIVv6lz'

        make_request_from_nasa_api = requests.get(nasa_apod_url + nasa_api_key)
        nasa_request_converted_to_json = make_request_from_nasa_api.json()
        print(nasa_request_converted_to_json)



        space_photo = self.create(
            #copyright=nasa_request_converted_to_json['copyright'],
            date=nasa_request_converted_to_json['date'],
            explanation=nasa_request_converted_to_json['explanation'],
            hdurl=nasa_request_converted_to_json['hdurl'],
            media_type=nasa_request_converted_to_json['media_type'],
            service_version=nasa_request_converted_to_json['service_version'],
            title=nasa_request_converted_to_json['title'],
            url=nasa_request_converted_to_json['url'] 
            )

        return space_photo


class SpacePhoto(models.Model): 
    #copyright = models.TextField(max_length=2000, null=True)
    date = models.DateTimeField(auto_now=True)
    explanation = models.TextField(max_length=2000, null=True)
    hdurl = models.CharField(max_length=180, null=True)
    media_type = models.TextField(max_length=50, null=True)
    service_version = models.CharField(max_length=2, null=True)
    title = models.TextField(max_length=50)
    url = models.CharField(max_length=180, null=True)

    objects = SpacePhotoManager()

