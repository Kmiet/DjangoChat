from django.core.files.storage import FileSystemStorage
from django.conf import settings as config
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Channel
# Create your views here.

User = get_user_model()

@login_required
def channel(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            try:
                Channel.objects.create_channel(name)
            except ValueError as e:
                e.args[0]

    return HttpResponseRedirect('/lobby')

@login_required
def settings(request):
    if request.method == 'POST':
        colour = request.POST.get('colour')
        avatar = request.FILES.get('avatar')
        user = User.objects.get(id=request.user.id)
        if avatar:
            user.avatar = 'avatar/' + request.user.username + '.png'
            fs = FileSystemStorage()
            location = config.MEDIA_ROOT + user.avatar
            fs.delete(location)
            fs.save(location, avatar)
        if colour:
            user.colour = colour

        user.save()

    return HttpResponseRedirect('/lobby')

@login_required
def chat(request, id):
     if request.method == 'GET':
        context = {
            'channelID': id,
            'user': {
                'colour': request.user.colour,
                'avatar': request.user.avatar,
                'name': request.user.username,
            }
        }
        try:
            context['title'] = Channel.objects.get(id = id).name
        except:
            return HttpResponseRedirect('/lobby')

        channels = Channel.objects.all()
        context['channels'] = channels

     return render(request, 'lobby.html', context)

@login_required
def lobby(request):
    context = {
        'title': 'Lobby',
        'user': {
            'colour': request.user.colour,
            'avatar': request.user.avatar,
            'name': request.user.username,
        }
    }

    channels = Channel.objects.all()
    context['channels'] = channels

    return render(request, 'lobby.html', context)