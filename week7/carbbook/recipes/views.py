from django.template import Context, loader
from django.http import HttpResponse, Http404
from recipes.models import Recipe
from django.shortcuts import render_to_response

def index(request):
	recipe_list = Recipe.objects.all()
	t = loader.get_template('recipe/index.html')
	c = Context({'recipe_list': recipe_list})
	return HttpResponse(t.render(c))

def category(request, category_name):
	recipe_list = Recipe.objects.filter(category=category_name)
	t = loader.get_template('recipe/category.html')
	c = Context({'recipe_list': recipe_list})
	return HttpResponse(t.render(c))

def detail(request, recipe_id):
	try:
		r = Recipe.objects.get(pk=recipe_id)
	except Recipe.DoesNotExist:
		raise Http404
	return render_to_response('recipe/detail.html', {'recipe': r})


