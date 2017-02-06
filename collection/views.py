from django.shortcuts import render

# Create your views here.
def index(request):
	number = 1
	thing = "Youssef"
	return render(request, 'index.html',{
		'number':number,
		'thing': thing,
	})