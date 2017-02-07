from django.shortcuts import render, redirect
from collection.models import Game
from collection.forms import GameForm

# Create your views here.
def index(request):
	games = Game.objects.all
	return render(request, 'index.html',{
		'games': games,
	})

def thing_detail(request, slug):
	game = Game.objects.get(slug=slug)
	return render(request, 'thing_detail.html',{
		'game':game,
	})

def edit_game(request, slug):
	game = Game.objects.get(slug=slug)
	form_class = GameForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=game)
		if form.is_valid():
			form.save()
			return redirect('thing_detail', slug=game.slug)
	else:
		form = form_class(instance = game)
	return render(request, 'edit_game.html',{
		'game':game,
		'form':form,
	
	})
