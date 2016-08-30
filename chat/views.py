from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from .models import Message
from .forms import MessageForm

from character.models import Character

import math, random

# Create your views here.

def index(request, page = 0):
    msgs_per_page = 2
    lastest_messages = Message.objects.order_by('-created')[ int(page) * msgs_per_page : ( int(page) + 1 ) * msgs_per_page ]
    context = {
        'messages' : lastest_messages,
        'form' : MessageForm(),
        'pagination' : pagination(math.ceil((len(Message.objects.all())-1) / msgs_per_page), page)
    }
    return render(request, 'chat/index.html', context)

def sendMessage(request, page = 0):
    errors = None
    success = None

    context = {}

    response = render_to_response('chat/send.html', request,  context)

    if 'character_id' not in request.COOKIES:
        response.set_cookie('character_id', Character.objects.all()[random.randint(0,len(Character.objects.all())-1)].id)

    if request.method == 'POST':
        character_id = request.COOKIES['character_id'];
        form = MessageForm(request.POST)
        if form.is_valid():
            form = MessageForm(request.POST, initial={'character_id': int(character_id)})
#            form.save()

            m = Message()
            m.message = request.POST['message']
            m.character_id = character_id
            m.save()
    else:
        form = MessageForm()



    return response

def pagination(all_pages_count, current_page, link_prefix = ''):
    result = []
    for i in range(0, int(all_pages_count)+1):
        link = Link()
        link.id = i
        link.title += str(i+1)
        link.page_prefix = link_prefix
        if i == current_page:
             link.is_current = True
        result += [ link ]
    return result

class Link:
    id = 0
    title = 'Page '
    is_current = False
    page_prefix = ''
