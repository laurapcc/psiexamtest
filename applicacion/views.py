from django.shortcuts import render
from .models import Usuario, Retweet


def usuario(request):
    rts = Retweet.objects.filter(tweet__usuario__id=1002)
    username = Usuario.objects.get(id=1002).username
    if rts:
        return render(request, 'usuario.html', {'retweets': rts, 'username': username})
    else:
        error = 'No hay tweets :('
        return render(request, 'usuario.html', {'error': error, 'username': username})
