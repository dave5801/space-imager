from django.http import HttpResponse
from django.template import loader
from space_imager_profile.models import Space_Photo_From_NASA


def home_view(request):
    """Home view callable, for the home page."""
    new_space_photo = Space_Photo_From_NASA.get_newly_created_photo.create_space_photo_from_nasa_api()
    print(new_space_photo.explanation)

    template = loader.get_template("space_imager_profile/home.html")
    response_body = template.render()
    return HttpResponse(response_body)


def home(request):
    """."""
    return HttpResponse("The home might display here")


def about(request):
     """."""
     return HttpResponse("Some other stuff might display here")