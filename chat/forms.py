from django import forms

from character.models import Character
from .models import Message

class MessageForm(forms.ModelForm):


    class Meta:
        model = Message
        fields = (
            'message',
        )
