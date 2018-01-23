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


class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book

class Book(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()

#book = Book.objects.create_book("Pride and Prejudice")

     

    '''
    def make_nasa_api_request_and_return_json(self, nasa_apod_url, nasa_api_key):
        make_request_from_nasa_api = requests.get(nasa_apod_url + nasa_api_key)
        nasa_request_converted_to_json = make_request_from_nasa_api.json()

        return nasa_request_converted_to_json

    def get_new_space_photo(self):

        #will become part of environ
        nasa_apod_url = 'https://api.nasa.gov/planetary/apod?api_key='
        nasa_api_key = 'sgQen3xfYyYvOzwtIn1QKeCe5SmHiFxLjdIVv6lz'

        nasa_space_photo_json = self.make_nasa_api_request_and_return_json(nasa_apod_url, nasa_api_key)

        return NASA_SpacePhoto_Template_Object(nasa_space_photo_json)
        '''


'''
class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        # do something with the book
        return book

class Book(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()
'''