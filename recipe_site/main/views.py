from recipes.models import Recipes
import random
from users.forms import UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def index(request):

    all_recipes = list(Recipes.objects.all())


    random_recipes = random.sample(all_recipes, min(len(all_recipes), 5))

    data = {
        'title': 'Главная страница!',
        'random_recipes': random_recipes,  # Передаем в шаблон
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect("home")  # Перенаправление на главную страницу
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})