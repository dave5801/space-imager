"""Make API call to NASA Astronomy Picture of the Day."""


import requests

class NASA_SpacePhoto_From_API_Object(object):
    """Call API convert to JSON and be ready to send to Models."""

    def __init__(self):

        make_request_from_nasa_api = requests.get('https://api.nasa.gov/planetary/apod?api_key=sgQen3xfYyYvOzwtIn1QKeCe5SmHiFxLjdIVv6lz')

        convert_request_from_nasa_api_to_json = make_request_from_nasa_api.json()

        self.copyright = convert_request_from_nasa_api_to_json['copyright']
        self.date = convert_request_from_nasa_api_to_json['date']
        self.explanation = convert_request_from_nasa_api_to_json['explanation']
        self.hdurl = convert_request_from_nasa_api_to_json['hdurl']
        self.media_type = convert_request_from_nasa_api_to_json['media_type']
        self.service_version = convert_request_from_nasa_api_to_json['service_version']
        self.title = convert_request_from_nasa_api_to_json['title']
        self.url = convert_request_from_nasa_api_to_json['url']

if __name__ == '__main__':
    space_photo = NASA_SpacePhoto_From_API_Object()
    print(space_photo.title)
    print(space_photo.url)
