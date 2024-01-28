from django.db import models

# Create your models here.
"""
Database
A list of products should be stored in the application database. A product has a name,
 as well as an integer field that stores information about how many times a dish has been cooked using that product. 

Recipes are also stored in the database.

The recipe has a name, as well as a set of products included in the recipe, indicating the weight in grams.

For example, the recipe Cheesecake, which includes the products Cottage cheese 200g, Egg 50g, Sugar 10g.

The same product can be used in different recipes. The same product cannot be used twice in the same recipe.
"""

class Product(models.Model):
    name = models.CharField(max_length=255)
    cooked_times = models.IntegerField()
    dishes = models.ManyToManyField('Recipe', through='RecipeProduct')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.recipe.name} - {self.product.name}"