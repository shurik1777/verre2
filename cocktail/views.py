from django.views import View
from django.shortcuts import render
from django.contrib import messages

from .forms import IngredientForm, CocktailForm, CategoryIngredientForm
from .models import Cocktail


def home_page(request):
    # Получаем 5 случайных коктейлей, не зависимо от авторизации
    recipes = Cocktail.objects.order_by('?')[:5]
    return render(request, 'cocktail/home.html', {'cocktail': recipes})


def recipe_detail(request, slug):
    recipe = Cocktail.objects.get(slug=slug)
    return render(request, 'cocktail/recipe_detail.html', {'cocktail': recipe})


def add_category(request):
    if request.method == 'POST':
        form = CategoryIngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана! 🎉')
            return render(request, 'cocktail/add_category.html', {'form': form})
    else:
        form = CategoryIngredientForm()
    return render(request, 'cocktail/add_category.html', {'form': form})


class AddIngredientView(View):
    def get(self, request):
        form = IngredientForm()
        return render(request, 'cocktail/add_ingredient.html', {'form': form})

    def post(self, request):
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            messages.success(request, 'Ингредиент успешно создан! 🎉')
            return render(request, 'cocktail/add_ingredient.html', {'form': form})
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
            messages.success(request, 'Ингредиент успешно создан! 🎉')
            return render(request, 'cocktail/add_category.html', {'form': form})
        return render(request, 'cocktail/add_category.html', {'form': form})
