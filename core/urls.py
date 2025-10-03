from django.contrib import admin
from django.urls import path, include
from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include('recipe.urls')),
    path('', views.recipe, name='recipes'),
    path('update_recipe/<id>', views.update_recipe, name='update_recipe'),
   path('delete_recipe/<id>', views.delete_recipe, name='delete_recipe'),
]