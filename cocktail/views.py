from django.shortcuts import render, redirect
from django.views import View

from .forms import IngredientForm, CocktailForm
from .models import Cocktail


def home_page(request):
    # Получаем 5 случайных коктейлей, не зависимо от авторизации
    recipes = Cocktail.objects.order_by('?')[:5]
    return render(request, 'home.html', {'cocktail': recipes})


def recipe_detail(request, slug):
    recipe = Cocktail.objects.get(slug=slug)
    return render(request, 'recipe_detail.html', {'cocktail': recipe})


class AddIngredientView(View):
    def get(self, request):
        form = IngredientForm()
        return render(request, 'cocktail/add_ingredient.html', {'form': form})

    def post(self, request):
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            return redirect('recipes:ingredients_list')
        return render(request, 'cocktail/add_ingredient.html', {'form': form})


class AddCocktailView(View):
    def get(self, request):
        form = CocktailForm()
        return render(request, 'cocktail/add_category.html', {'form': form})

    def post(self, request):
        form = CocktailForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('recipes:categories_list')
        return render(request, 'cocktail/add_category.html', {'form': form})
