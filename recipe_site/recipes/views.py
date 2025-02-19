from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def recipes_home(request):
    recipes = Recipes.objects.order_by('title')
    return render(request, 'recipes/recipes_home.html', {'recipes': recipes})

class RecipesDetailView(DetailView):
    model = Recipes
    template_name = 'recipes/details_view.html'
    context_object_name = 'recipe'

class RecipesUpdateView(UpdateView):
    model = Recipes
    template_name = 'recipes/create.html'

    form_class = RecipesForm

class RecipesDeleteView(DeleteView):
    model = Recipes
    success_url = '/recipes/'
    template_name = 'recipes/recipes_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = RecipesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes_home')
        else:
            error = 'Форма была неверной'

    form = RecipesForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'recipes/create.html', data)