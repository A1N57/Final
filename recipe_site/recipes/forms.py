from django.forms import ModelForm, TextInput, Textarea, NumberInput, ClearableFileInput
from .models import Recipes


class RecipesForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'description', 'steps', 'cooking_time', 'ingredients', 'image']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название рецепта'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'steps': Textarea(attrs={'class': 'form-control', 'placeholder': 'Шаги приготовления'}),
            'cooking_time': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Время приготовления (мин)'}),
            'ingredients': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ингредиенты'}),
            'image': ClearableFileInput(attrs={'class': 'form-control'}),
        }
