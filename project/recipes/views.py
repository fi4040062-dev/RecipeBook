from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import RecipeForm
from .models import Recipe


def home(request):
    return render(request, 'recipes/home.html')


def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, rec_id):
    recipe = get_object_or_404(Recipe, id=rec_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_recipes')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_add.html',
                  {'form': form, 'title': 'Add recipe'})


@login_required
def edit_recipe(request, rec_id):
    recipe = get_object_or_404(Recipe, id=rec_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('all_recipes')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_add.html',
                  {'form': form, 'title': 'Editing recipe'})


@login_required
@require_POST
def delete_recipe(request, rec_id):
    recipe = get_object_or_404(Recipe, id=rec_id)
    recipe.delete()
    return redirect('all_recipes')


        
    

















# Create your views here.
