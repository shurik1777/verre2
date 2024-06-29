from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
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
            messages.success(request, 'Коктейль успешно создан! 🎉')
            return render(request, 'cocktail/add_category.html', {'form': form})
        return render(request, 'cocktail/add_category.html', {'form': form})


def all_receipt(request):
    cocktail = Cocktail.objects.all()
    return render(request, "cocktail/all_receipt.html", {'cocktail': cocktail})


def get_receipt(request):
    if request.method == 'GET':
        form = CocktailForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            recipes = (Cocktail.objects.filter(name__icontains=search_query) | Cocktail.objects.filter(
                description__icontains=search_query))
            return render(request, 'cocktail/recipe_search_results.html',
                          {'recipes': recipes, 'search_query': search_query})
    else:
        form = CocktailForm()
    return render(request, "cocktail/get_receipt.html", {'form': form})


def cocktail_detail(request, cocktail_id):
    cocktail = get_object_or_404(Cocktail, pk=cocktail_id)
    return render(request, 'cocktail/recipe_detail.html', {'receipt': cocktail})


def modify_cocktail(request, cocktail_id):
    cocktail = get_object_or_404(Cocktail, pk=cocktail_id)
    if request.method == 'POST':
        form = CocktailForm(request.POST, request.FILES, instance=cocktail)
        if form.is_valid():
            form.save()
            return redirect('receipt_detail', receipt_id=cocktail.id)
    else:
        form = CocktailForm(instance=cocktail)
    return render(request, "cocktail/add_recipe.html", {'form': form})
