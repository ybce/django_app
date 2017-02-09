from django.forms import ModelForm
from collection.models import Game

class GameForm(ModelForm):
	class Meta:
		model = Game
		fields = ('name','description')