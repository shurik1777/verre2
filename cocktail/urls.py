from django.urls import path
from . import views
from .views import AddIngredientView, AddCocktailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cocktail'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_ingredients/', AddIngredientView.as_view(), name='add_ingredient'),
    path('add_receipt/', AddCocktailView.as_view(), name='add_recipe'),
    path('all_cocktails/', views.all_cocktails, name='all_cocktails'),
    path('cocktails/<slug:cocktail_slug>/', views.all_cocktails, name='all_cocktails'),
    path('cocktails/<slug:cocktail_slug>/', views.show_cocktail, name='show_cocktail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
