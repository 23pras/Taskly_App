import os
from django.db import models
from django.contrib.auth.models import User 
from django.utils.deconstruct import deconstructible 


# Create your models here.
@deconstructible
class GenerateProfileImagePath(object):

    def __init__(self):
        pass
    
    def __call__(self,instance,filename):
        ext = filename.split('.')[-1]                             #taking the extension of uploaded image file.
        path = f'media/accounts/{instance.user.id}/images/'       #instance here used as a reference for profiles.
        name = f'profile_image.{ext}'                          # extension extracted and stored into another variable with the help of string interpolation.
        return os.path.join(path, name)                        #adding the patha and extracted name here.


user_profile_image_path = GenerateProfileImagePath()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)               # models.CASACADE will deleted the profile with user.
    image = models.FileField(upload_to=user_profile_image_path, blank=True, null=True)  #inside upload we have defind path to store image.

    def __str__(self):
        return  f'{self.user.username}\'s Profile'                   #used it so that user name can be displayed instead of just profile object.


