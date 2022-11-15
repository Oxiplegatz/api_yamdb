# from django.contrib.auth import get_user_model
from django.db import models

# User = get_user_model()


class Genre(models.Model):
    """Модель хранящая данные о жанрах."""
    name = models.CharField('Название жанра', max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Модель хранящая данные о категориях."""
    name = models.CharField('Название категории', max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель хранящая данные о произведениях."""
    name = models.CharField('Название произведения', max_length=256)
    year = models.DateField(
        'Год выхода', input_formats=['%Y', 'iso-8601'], format='%Y'
    )
    rating = models.IntegerField(
        'Рейтинг', default=None, required=False, max_value=10, min_value=1
    )
    description = models.TextField('Описание произведения', required=False)
    genre = models.ManyToManyField(
        Genre, through='GenreTitle', blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='titles'
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    """Модель, релизующая связь многие-ко-многим Произведений и Жанров."""
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'
