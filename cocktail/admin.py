from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CategoryCocktail, CategoryIngredient

admin.site.site_header = 'Verre - сайт рецептов алкогольных напитков'
admin.site.site_title = 'Администрирование сайта'
admin.site.index_title = 'Администрирование сайта'


@admin.register(CategoryCocktail)
class CategoryCocktailAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', "slug")
    list_display_links = ('name',)
    list_editable = ["slug", ]
    search_fields = ('name', "slug")
    fields = [
        "name",
        "slug",
    ]


@admin.register(CategoryIngredient)
class CategoryIngredientAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', "slug")
    list_display_links = ('name',)
    list_editable = ["slug", ]
    search_fields = ('name', "slug")
    fields = [
        "name",
        "slug",
    ]
