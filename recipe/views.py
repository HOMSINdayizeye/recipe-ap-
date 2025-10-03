from django.shortcuts import render,redirect, get_object_or_404
from .models import Recipe


# Create your views here.
def recipe(request):
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
  
        Recipe.objects.create(
        recipe_name = recipe_name,
        recipe_description = recipe_description,
        recipe_image = recipe_image,
        )
        return redirect('/recipe/')  # or wherever you want to go

    #  This handles GET requests
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipes.html', {'recipes': recipes})



def delete_recipe(request, id):
    recipe= get_object_or_404(Recipe, id = id)
    recipe.delete()
    return redirect('/')


def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id = id)
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        
        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description
    if recipe_image:
       recipe.recipe_image = recipe_image
    recipe.save()
    context = {'recipe': 'recipe'}

    return redirect('/recipe/')
    return render(request, 'update_recipe.html', context) 
        
