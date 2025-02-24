from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipes
from .forms import RecipesForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def recipes_home(request):
    recipes = Recipes.objects.all().order_by('-date')
    return render(request, 'recipes/recipes_home.html', {'recipes': recipes})


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

    def dispatch(self, request, *args, **kwargs):
        """Ограничиваем доступ к редактированию только автору рецепта"""
        obj = self.get_object()
        if obj.author != self.request.user:
            messages.error(self.request, "Вы не можете редактировать этот рецепт, так как вы не его автор.")
            return redirect('recipes_home')  # Перенаправляем на страницу списка рецептов
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()


class RecipesDeleteView(LoginRequiredMixin, DeleteView):
    """Страница удаления рецепта"""
    model = Recipes
    template_name = 'recipes/recipes_delete.html'
    success_url = reverse_lazy('recipes_home')

    def dispatch(self, request, *args, **kwargs):
        """Ограничиваем доступ к удалению только автору рецепта"""
        obj = self.get_object()
        if obj.author != self.request.user:
            messages.error(self.request, "Вы не можете удалить этот рецепт, так как вы не его автор.")
            return redirect('recipes_home')  # Перенаправляем на страницу списка рецептов
        return super().dispatch(request, *args, **kwargs)

