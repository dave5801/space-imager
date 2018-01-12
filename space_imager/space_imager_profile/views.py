from django.http import HttpResponse
from django.template import loader
from space_imager_profile.nasa_api_call import call_nasa_url_return_photo_url, retrieve_from_photo_url_and_save_in_dir

SPACE_PHOTO_URL = call_nasa_url_return_photo_url()
retrieve_from_photo_url_and_save_in_dir(SPACE_PHOTO_URL)


def home_view(request):
    """Home view callable, for the home page."""
    template = loader.get_template("space_imager_profile/home.html")
    response_body = template.render()
    return HttpResponse(response_body)

# Create your views here.
'''
def index(request):
    return HttpResponse("Hello, world. This is the Space Imager")
    '''

def home(request):
    return HttpResponse("The home might display here")

def about(request):
     return HttpResponse("Some other stuff might display here")