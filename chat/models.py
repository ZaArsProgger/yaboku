from __future__ import unicode_literals

from django.db import models

from character.models import Character

import random

# Create your models here.

class Message(models.Model):
    character = models.ForeignKey(Character, models.SET_NULL, blank=True, null=True)

    message     = models.TextField(blank=False)
    created     = models.DateTimeField(auto_now_add=True)

    def is_fine_message(self, min_length = 5):
        if len(self.message) >= min_length:
            return True
        else:
            return False
