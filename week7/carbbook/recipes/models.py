from django.db import models

class Recipe(models.Model):
	CATEGORY_CHOICES = (
		('Breakfast', 'Breakfast'),
		('Lunch', 'Lunch'),
		('Snack', 'Snack'),
		('Dinner', 'Dinner'),
		('Dessert', 'Dessert'),
	)
	name = models.CharField(max_length=30)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
	protein = models.IntegerField()
	net_carbs = models.IntegerField()
	def __unicode__(self):
                return self.name	

class Ingredient(models.Model):
	SIZE_CHOICES = (
        	('C', 'Cup(s)'),
        	('Tbs', 'Tablespoon(s)'),
		('Tsp', 'Teaspoon(s)'),
		('None', 'None'),
	)
	recipe = models.ForeignKey(Recipe)
	name = models.CharField(max_length=20)
	amount = models.IntegerField()
	size = models.CharField(max_length=10, choices=SIZE_CHOICES)
