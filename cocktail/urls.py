from django.urls import path
from . import views
from .views import AddIngredientView, AddCocktailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cocktail'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add_category/', views.add_category, name='add_category'),
    path('ingredients/add/', AddIngredientView.as_view(), name='add_ingredient'),
    path('add_receipt/', AddCocktailView.as_view(), name='add_recipe'),
    path('recipe/', views.cocktail_detail, name='cocktail_detail'),
    path('all_receipt/', views.all_receipt, name='all_receipt'),
    path('get_receipt/', views.get_receipt, name='get_receipt'),
    path('cocktail_detail/', views.cocktail_detail, name='cocktail_detail'),
    path('cocktail_detail/<int:cocktail_id>/', views.cocktail_detail, name='cocktail_detail'),
    path('modify_cocktail/<int:cocktail_id>/', views.modify_cocktail, name='modify_cocktail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
