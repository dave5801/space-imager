"""Model for a Space Photo taken from NASA."""

from django.db import models
import os
import requests

#look into init method for a model
#that's where the api request should go

class Create_A_New_Space_Photo_from_NASA_API(models.Manager):
    def create_space_photo_from_nasa_api(self):
        nasa_apod_url_from_environment_variables = os.environ.get('NASA_APOD_URL', '')
        nasa_api_key_from_environment_variables = os.environ.get('NASA_API_KEY', '')

        get_response_from_nasa_api_request = requests.get(nasa_apod_url_from_environment_variables
         + nasa_api_key_from_environment_variables)

        get_response_from_nasa_api_request_converted_to_json = get_response_from_nasa_api_request.json()

        a_new_space_photo = self.create(
            date=get_response_from_nasa_api_request_converted_to_json['date'],
            explanation=get_response_from_nasa_api_request_converted_to_json['explanation'],
            hdurl=get_response_from_nasa_api_request_converted_to_json['hdurl'],
            media_type=get_response_from_nasa_api_request_converted_to_json['media_type'],
            service_version=get_response_from_nasa_api_request_converted_to_json['service_version'],
            title=get_response_from_nasa_api_request_converted_to_json['title'],
            url=get_response_from_nasa_api_request_converted_to_json['url'] 
            )

        return a_new_space_photo
 
class Space_Photo_From_NASA(models.Model): 
    date = models.DateTimeField(auto_now=True)
    explanation = models.TextField(max_length=2000, null=True)
    hdurl = models.CharField(max_length=180, null=True)
    media_type = models.TextField(max_length=50, null=True)
    service_version = models.CharField(max_length=2, null=True)
    title = models.TextField(max_length=50)
    url = models.CharField(max_length=180, null=True)

    get_newly_created_photo = Create_A_New_Space_Photo_from_NASA_API()

