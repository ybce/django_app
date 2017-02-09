from django.shortcuts import render, redirect
from collection.models import Game
from collection.forms import GameForm
from django.template.defaultfilters import slugify

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

@login_required
def edit_game(request, slug):
	game = Game.objects.get(slug=slug)
	if game.user != request.user:
		raise Http404
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

def create_game(request):
	form_class = ThingForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            thing = form.save(commit=False)

            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)

            # save the object
            thing.save()

            # redirect to our newly created thing
            return redirect('thing_detail', slug=thing.slug)
			# otherwise just create the form
    else:
        form = form_class()

    return render(request, ‘things/create_thing.html', {
        'form': form,
    })
