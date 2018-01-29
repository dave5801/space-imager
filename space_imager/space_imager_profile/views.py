from django.http import HttpResponse
from django.template import loader
from space_imager_profile.models import Space_Photo_From_NASA
from space_imager_profile.nasa_api_interface import NASASpacePhotoAPICallInterface


def home_view(request):
    """Home view callable, for the home page."""
    new_space_photo = NASASpacePhotoAPICallInterface()
    print(new_space_photo.get_response_from_nasa_api_request_converted_to_json)

    template = loader.get_template("space_imager_profile/home.html")
    response_body = template.render()
    return HttpResponse(response_body)


def home(request):
    """."""
    return HttpResponse("The home might display here")


def about(request):
     """."""
     return HttpResponse("Some other stuff might display here")