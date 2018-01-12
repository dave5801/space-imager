"""Calling Nasa API."""

from urllib.request import urlopen
import urllib.request
import json
from datetime import datetime


def call_nasa_url_return_photo_url():
    """."""
    nasa_apod_url = "https://api.nasa.gov/planetary/apod?api_key=sgQen3xfYyYvOzwtIn1QKeCe5SmHiFxLjdIVv6lz"

    response = urlopen(nasa_apod_url)
    response_parse_to_string = response.read().decode('utf-8')
    nasa_response_json_obj = json.loads(response_parse_to_string)

    return nasa_response_json_obj['url']


def retrieve_from_photo_url_and_save_in_dir(photo_url):
    """."""
    download_space_photo_file_path = "static/space_photos/space_photo1" + str(datetime.now()) +".jpg"
    urllib.request.urlretrieve(photo_url, download_space_photo_file_path) #save in dir


if __name__ == '__main__':
    photo_url = call_nasa_url_return_photo_url()
    retrieve_from_photo_url_and_save_in_dir(photo_url)
