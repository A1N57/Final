from django.db import models
from django.contrib.auth.models import User



class Recipes(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', default='')
    steps = models.TextField('Шаги приготовления', default='')
    cooking_time = models.PositiveIntegerField('Время приготовления (мин)')
    ingredients = models.TextField('Ингредиенты', default='')
    image = models.ImageField('Изображение', upload_to='recipes/', blank=True, null=True)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/recipes/{self.id}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
