from django.contrib import admin

# Register your models here.
from .models import Product, Recipe, RecipeProduct

admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(RecipeProduct)