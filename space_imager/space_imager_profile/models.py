"""Model for a Space Photo taken from NASA."""

from django.db import models
import os
import requests

class SpacePhotoManager(models.Manager):
    def create_space_photo(self):
        nasa_apod_url = os.environ.get('NASA_APOD_URL', '')
        nasa_api_key = os.environ.get('NASA_API_KEY', '')

        make_request_from_nasa_api = requests.get(nasa_apod_url + nasa_api_key)
        nasa_request_converted_to_json = make_request_from_nasa_api.json()

        '''Note - copyright field not in every NASA photo - revisit to later'''
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

