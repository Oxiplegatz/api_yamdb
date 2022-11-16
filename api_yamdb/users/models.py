from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя. Поля email и username обязательны
    и должны быть уникальными.
    """
    ROLE_CHOICES = (
        (1, 'user'),
        (2, 'admin'),
        (3, 'moderator'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    bio = models.TextField(
        'О себе',
        max_length=500,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


CustomUser._meta.get_field('username').max_length = 150
CustomUser._meta.get_field('email').max_length = 254
CustomUser._meta.get_field('email')._unique = True
