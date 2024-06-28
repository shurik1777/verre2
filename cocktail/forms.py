from django import forms

from cocktail.models import Ingredient, Cocktail, CategoryIngredient, CategoryCocktail


class CategoryIngredientForm(forms.ModelForm):
    class Meta:
        model = CategoryIngredient
        fields = ['name', 'slug']


class CategoryCocktailForm(forms.ModelForm):
    class Meta:
        model = CategoryCocktail
        fields = ['name', 'slug']


class IngredientForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=CategoryIngredient.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )

    class Meta:
        model = Ingredient
        fields = [
            'name',
            'slug',
            'description',
            'image',
            'categories'
        ]


class CocktailForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=CategoryCocktail.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Cocktail
        fields = [
            'title',
            'slug',
            'description',
            'preparation_steps',
            'preparation_time',
            'image',
            'author',
            'categories',
        ]
