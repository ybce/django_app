from django.shortcuts import render
from collection.models import Game

# Create your views here.
def index(request):
	games = Game.objects.all
	return render(request, 'index.html',{
		'games': games,
	})