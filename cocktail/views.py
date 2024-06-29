from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import IngredientForm, CocktailForm, CategoryIngredientForm
from .models import Cocktail


def home_page(request):
    # Получаем 5 случайных коктейлей, не зависимо от авторизации
    recipes = Cocktail.objects.order_by('?')[:5]
    return render(request, 'cocktail/home.html', {'cocktail': recipes})


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
    model = Cocktail

    def get(self, request):
        form = CocktailForm()
        return render(request, 'cocktail/add_category.html', {'form': form})

    def post(self, request):
        form = CocktailForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, 'Коктейль успешно создан! 🎉')
            return render(request, 'cocktail/add_category.html', {'form': form})
        return render(request, 'cocktail/add_category.html', {'form': form})


def all_cocktails(request):
    cocktails = Cocktail.objects.all()
    context = {
        'cocktails': cocktails
    }
    return render(request, 'cocktail/all_cocktails.html', context)


def cocktail_detail(request, slug):
    cocktail = get_object_or_404(Cocktail, slug=slug)

    context = {
        'cocktail': cocktail
    }
    return render(request, 'cocktail/cocktail_detail.html', context)
