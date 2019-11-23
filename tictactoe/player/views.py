from django.shortcuts import render

from gameplay.models import Game

# Create your views here.

def home(request):
    my_games = Game.objects.games_for_users(request.user)
    active_games = my_games.active()
    return render(request, "player/home.html",
                  {'message': "Hi, There", 'games': Game.objects.all()})
