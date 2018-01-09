from django.http import HttpResponse
#from django.shortcuts import render
from django.template import loader


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
