from django.shortcuts import render
from django.http import Http404

from .models import Character

# Create your views here.

def detail(request, character_id):
    try:
        character = Character.objects.get(pk=character_id)
    except:
        raise Http404("Char no exists")
    return render(request, 'character/detail.html', {
        'character' : character,
    })
