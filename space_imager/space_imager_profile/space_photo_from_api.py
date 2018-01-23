"""Make API call to NASA Astronomy Picture of the Day."""

import requests


class NASA_SpacePhoto_Template_Object(object):
    """Call API convert to JSON and be ready to send to Models."""
    """Note: JSON doesn't always have all desired properites, hence if statements."""
    def __init__(self, nasa_request_converted_to_json=None):
        if 'copyright' in nasa_request_converted_to_json:
            self.copyright = nasa_request_converted_to_json['copyright']
        else:
            self.copyright = ''

        if 'date' in nasa_request_converted_to_json:
            self.date = nasa_request_converted_to_json['date']
        else:
            self.date = ''

        if 'explanation' in nasa_request_converted_to_json:
            self.explanation = nasa_request_converted_to_json['explanation']
        else:
            self.date = ''

        if 'hdurl' in nasa_request_converted_to_json:
            self.hdurl = nasa_request_converted_to_json['hdurl']
        else:
            self.date = ''

        if 'media_type' in nasa_request_converted_to_json:
            self.media_type = nasa_request_converted_to_json['media_type']
        else:
            self.media_type = ''

        if 'service_version' in nasa_request_converted_to_json:
            self.service_version = nasa_request_converted_to_json['service_version']
        else:
            self.service_version = ''

        if 'title' in nasa_request_converted_to_json:
            self.title = nasa_request_converted_to_json['title']
        else:
            self.title = ''

        if 'url' in nasa_request_converted_to_json:
            self.url = nasa_request_converted_to_json['url']
        else:
            self.url = ''


class NASA_Space_Photo_DTO(object):
    """Look into Data Transfer Object Patter."""
    """This packages up api data to send to models."""

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

if __name__ == '__main__':

    nasa_space_photo_dto = NASA_Space_Photo_DTO()
    new_space_photo = nasa_space_photo_dto.get_new_space_photo()

    print(new_space_photo.title)
    print(new_space_photo.url)
