import os
import requests


class NASASpacePhotoAPICallInterface(object):

    def __init__(self):
        nasa_apod_url_from_environment_variables = os.environ.get('NASA_APOD_URL', '')
        nasa_api_key_from_environment_variables = os.environ.get('NASA_API_KEY', '')

        self.get_response_from_nasa_api_request = requests.get(nasa_apod_url_from_environment_variables
         + nasa_api_key_from_environment_variables)

        self.get_response_from_nasa_api_request_converted_to_json = self.get_response_from_nasa_api_request.json()

if __name__ == '__main__':
    new_space_photo = NASASpacePhotoAPICallInterface()
    print(new_space_photo.get_response_from_nasa_api_request_converted_to_json)


