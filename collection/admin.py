from django.contrib import admin

# Register your models here.
from collection.models import Game


class GameAdmin(admin.ModelAdmin):
	model = Game
	list_display = ('name', 'description')
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Game,GameAdmin)