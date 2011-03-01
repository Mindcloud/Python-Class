from recipes.models import Recipe,Ingredient
from django.contrib import admin

class IngredientInline(admin.TabularInline):
	model = Ingredient
	extra = 2

class RecipeAdmin(admin.ModelAdmin):
	inlines = [IngredientInline]
	search_fields = ['category', 'name']
	list_display = ('name', 'category', 'net_carbs')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)

