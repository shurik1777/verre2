from django.urls import path
from . import views
# from .views import AddIngredientView, AddCategoryView, AddRecipeView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cocktail'

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('categories/add/', AddCategoryView.as_view(), name='add_category'),
    # path('ingredients/add/', AddIngredientView.as_view(), name='add_ingredient'),
    # path('recipes/add/', AddRecipeView.as_view(), name='add_recipe'),
    path('recipe/<slug:recipe_slug>/', views.recipe_detail, name='recipe_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
