from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_home, name='recipes_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.RecipesDetailView.as_view(), name='recipes-detail'),
    path('<int:pk>/update', views.RecipesUpdateView.as_view(), name='recipes-update'),
    path('<int:pk>/delete', views.RecipesDeleteView.as_view(), name='recipes-delete')
]