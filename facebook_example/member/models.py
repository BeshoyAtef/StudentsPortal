from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_facebook.models import FacebookModel, get_user_model
from django_facebook.utils import get_profile_model
import logging
logger = logging.getLogger(__name__)
from django_facebook.models import *

from django.db import models 
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel 
from django.db.models.signals import post_save 
from django_facebook.utils import get_user_model, get_profile_model 
from facebook_example import settings


try:
    # There can only be one custom user model defined at the same time
    if getattr(settings, 'AUTH_USER_MODEL', None) == 'member.CustomFacebookUser':
        from django.contrib.auth.models import AbstractUser, UserManager
        class CustomFacebookUser(AbstractUser, FacebookModel):
            '''
            The django 1.5 approach to adding the facebook related fields
            '''
            objects = UserManager()
            # add any customizations you like
            state = models.CharField(max_length=255, blank=True, null=True)
except ImportError as e:
    logger.info('Couldnt setup FacebookUser, got error %s', e)
    pass


# Create your models here.
class UserProfile(FacebookModel):
    '''
    Inherit the properties from django facebook
    '''
    mobilenumber = models.CharField(max_length=20 , null=True)
    email2 = models.EmailField(max_length=254, unique=True)
    user = models.IntegerField(blank=False,unique=True)

class MyCustomProfile(models.Model):
    '''
    Inherit the properties from django facebook
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    mobilenumber = models.CharField(max_length=20 , null=True)
    email2 = models.EmailField(max_length=254, unique=True)
    # user_id = models.IntegerField(blank=False,unique=True)

@receiver(post_save)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if sender == get_user_model():
        user = instance
        profile_model = get_profile_model()
        if profile_model == UserProfile and created:
            profile, new = UserProfile.objects.get_or_create(user=instance)

# class MyCustomProfile(FacebookModel):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)

# @receiver(post_save) 
# def create_profile(sender, instance, created, **kwargs):
# # Create a matching profile whenever a user object is created.
#     if sender == get_user_model():
#     user = instance 
#     profile_model = get_profile_model() 
#     if profile_model == MyCustomProfile and created:
#         profile, new = MyCustomProfile.objects.get_or_create(user=instance)
