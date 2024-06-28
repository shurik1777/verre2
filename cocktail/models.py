from django.db import models as m


class CategoryCocktail(m.Model):
    name = m.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return f"Категория: {self.name}, slug{self.slug}"

    class Meta:
        verbose_name = 'Категория коктейля'
        verbose_name_plural = 'Категории коктейлей'
        ordering = ("id",)


class CategoryIngredient(m.Model):
    name = m.CharField(max_length=120, unique=True, verbose_name='Название')
    slug = m.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return f"Категория: {self.name}, slug{self.slug}"

    class Meta:
        verbose_name = 'Категория ингредиента'
        verbose_name_plural = 'Категории ингредиентов'
        ordering = ("id",)
