from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all_recipes, name='all_recipes'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('<int:rec_id>/', views.recipe_detail, name='recipe_detail'),
    path('<int:rec_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('<int:rec_id>/delete/', views.delete_recipe, name='delete_recipe'),
]