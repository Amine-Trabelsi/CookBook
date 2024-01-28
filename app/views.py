from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    # Retrieve the recipe and product objects
    recipe = Recipe.objects.get(id=recipe_id)
    product = Product.objects.get(id=product_id)

    # Check if the recipe already contains the product
    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    
    # Update the weight
    recipe_product.weight = weight
    recipe_product.save()

    return HttpResponse("Product added to recipe successfully.")

def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')

    # Retrieve the recipe object
    recipe = Recipe.objects.get(id=recipe_id)

    # Get all products in the recipe
    products = recipe.products.all()

    # Increase the number of cooked dishes for each product
    for product in products:
        product.dishes.add(recipe)

    return HttpResponse("Recipe cooked successfully.")


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')

    # Retrieve the product object
    product = Product.objects.get(id=product_id)

    # Get recipes without the specified product or with a quantity less than 10 grams
    recipes = Recipe.objects.exclude(products=product) \
                           .exclude(recipeproduct__product=product, recipeproduct__weight__gte=10)

    context = {
        'recipes': recipes
    }

    return render(request, 'app/recipes_without_product.html', context)