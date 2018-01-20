"""."""

from django.db import models
from django.dispatch import receiver
from space_imager_profile.space_photo_from_api import NASA_SpacePhoto_From_API_Object
from django.contrib.auth.models import User


class Space_Photo_From_API_Model(models.Model, NASA_SpacePhoto_From_API_Object):
    """Model for a Space Photo."""
    copyright = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True)
    explanation = models.TextField(max_length=2000)
    hdurl = models.CharField(max_length=180)
    media_type = models.TextField(max_length=50)
    service_version = models.CharField(max_length=2)
    title = models.TextField(max_length=50)
    url = models.CharField(max_length=180)

    def __str__(self):
        """Print function returns title of photo."""
        return self.title

@receiver(models.signals.post_save, sender=User)
def create_space_photo_from_api_object(sender, **kwargs):
    """Create the profile when a user is created."""
    if kwargs['created']:
        space_photo_from_api_object = Space_Photo_From_API_Model(user=kwargs['instance'])
        space_photo_from_api_object.save()



'''EXAMPLE
from django.db import models
from django.dispatch import receiver
from emotion_profile.models import User
from emotion_authentication.face_verification import FaceVerification


# Create your models here.
class FaceVerificationManager(models.Model, FaceVerification):
    objects = models.Manager
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='faces')
    auth_face = models.ImageField(upload_to='auth_faces',
                                  blank=True,
                                  null=True)
    auth_face_id = models.CharField(blank=True,null=True,max_length=36)

    auth_last_recorded = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        """Print function returns this."""
        return self.user.username


@receiver(models.signals.post_save, sender=User)
def create_face_verification_object(sender, **kwargs):
    """Create the profile when a user is created."""
    if kwargs['created']:
        face_verification_object = FaceVerificationManager(user=kwargs['instance'])
        face_verification_object.save()
'''
