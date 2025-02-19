from django.db import models

class Recipes(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Рецепт')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/recipes/{self.id}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
