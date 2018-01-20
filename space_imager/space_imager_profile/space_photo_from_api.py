"""Make API call to NASA Astronomy Picture of the Day."""


import requests

class NASA_SpacePhoto_From_API_Object(object):
    """Call API convert to JSON and be ready to send to Models."""
    def __init__(self, nasa_request_converted_to_json=None):
        self.copyright = nasa_request_converted_to_json['copyright']
        self.date = nasa_request_converted_to_json['date']
        self.explanation = nasa_request_converted_to_json['explanation']
        self.hdurl = nasa_request_converted_to_json['hdurl']
        self.media_type = nasa_request_converted_to_json['media_type']
        self.service_version = nasa_request_converted_to_json['service_version']
        self.title = nasa_request_converted_to_json['title']
        self.url = nasa_request_converted_to_json['url']

if __name__ == '__main__':
    make_request_from_nasa_api = requests.get('https://api.nasa.gov/planetary/apod?api_key=sgQen3xfYyYvOzwtIn1QKeCe5SmHiFxLjdIVv6lz')
    nasa_request_converted_to_json = make_request_from_nasa_api.json()
    
    space_photo = NASA_SpacePhoto_From_API_Object(nasa_request_converted_to_json)
    
    print(space_photo.title)
    print(space_photo.url)
