from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins

from reviews.models import Genre, Category, Title
from .serializers import (
    GenreSerializer, CategorySerializer, TitleSerializer, TitlePostSerializer
)


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """Вьюсет для модели Genre."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = ('slug')

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Genre, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """Вьюсет для модели Category."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = ('slug')

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Genre, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Title."""
    queryset = Title.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'year', 'genre__slug', 'category__slug')

    def get_serializer_class(self):
        list = ['create', 'update', 'partial_update']
        if self.action in list:
            return TitlePostSerializer
        return TitleSerializer
