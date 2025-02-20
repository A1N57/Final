from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipes
from .forms import RecipesForm
import random


def recipes_home(request):
    """Главная страница с 5 случайными рецептами"""
    recipes = Recipes.objects.all()
    random_recipes = random.sample(list(recipes), min(len(recipes), 5))
    return render(request, 'recipes/recipes_home.html', {'random_recipes': random_recipes})


class RecipesDetailView(DetailView):
    """Страница подробного рецепта"""
    model = Recipes
    template_name = 'recipes/details_view.html'
    context_object_name = 'recipe'


class RecipesCreateView(LoginRequiredMixin, CreateView):
    """Страница добавления рецепта"""
    model = Recipes
    form_class = RecipesForm
    template_name = 'recipes/create.html'
    success_url = reverse_lazy('recipes_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = None  # Добавляем, чтобы избежать ошибки
        return context


class RecipesUpdateView(LoginRequiredMixin, UpdateView):
    """Страница редактирования рецепта (использует create.html)"""
    model = Recipes
    form_class = RecipesForm
    template_name = 'recipes/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class RecipesDeleteView(LoginRequiredMixin, DeleteView):
    """Страница удаления рецепта"""
    model = Recipes
    template_name = 'recipes/recipes_delete.html'
    success_url = reverse_lazy('recipes_home')

