from django.http import HttpResponse
from django.template import loader
#from emotion_authentication.models import FaceVerificationManager
from space_imager_profile.models import SpacePhoto, SpacePhotoManager


def home_view(request):
    """Home view callable, for the home page."""
    space_photo = SpacePhoto.objects.create_space_photo()
    print(space_photo.explanation)

    template = loader.get_template("space_imager_profile/home.html")
    response_body = template.render()
    return HttpResponse(response_body)


def home(request):
    """."""
    return HttpResponse("The home might display here")


def about(request):
     """."""
     return HttpResponse("Some other stuff might display here")