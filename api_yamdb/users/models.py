from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя. Поля email и username обязательны
    и должны быть уникальными.
    """
    CHOICES = (
        ('user', 'user'),
        ('admin', 'admin'),
        ('moderator', 'moderator'),
    )
    role = models.CharField(
        max_length=50,
        default='user',
        choices=CHOICES
    )
    bio = models.TextField(
        'О себе',
        max_length=500,
        blank=True
    )
    confirmation_code = models.CharField(
        max_length=8,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username)

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'


CustomUser._meta.get_field('username').max_length = 150
CustomUser._meta.get_field('email').max_length = 254
CustomUser._meta.get_field('email')._unique = True
