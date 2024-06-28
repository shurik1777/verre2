from django import forms

from cocktail.models import Ingredient, Cocktail


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'name',
            'slug',
            'description',
            'image'
        ]


class CocktailForm(forms.ModelForm):
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
        ]
