from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Created by DEV-B.

def get_upload_path(instance, filename):
    return f'mainapp/media/logos/{instance.user.id}/{filename}'

class Shop(models.Model):
    ''' Shop class : to store user's shop information.
        WARNING : Do not create instance of the class,
        without User model specified.
    '''
    BLANK = ''
    INT_BLANK = 0

    # Required
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shops', blank=True, null=True)

    name = models.CharField(max_length=128, blank=True)
    shop_type = models.CharField(max_length=64, blank=True)
    capacity = models.PositiveIntegerField(default=INT_BLANK)
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=256, blank=True)
    # location_field, to add later

    logo = models.ImageField(upload_to=get_upload_path ,default='mainapp/media/logos/default.png')

    def __str__(self):
        return f"{self.name}"
