from __future__ import unicode_literals

from django.db import models

#from chat.models import Message
#from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='character/', blank=False, default='character/no-image.png')


