# recipe/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe, name='recipes'),
    path('update/<int:id>/', views.update_recipe, name='update_recipe'),
]
