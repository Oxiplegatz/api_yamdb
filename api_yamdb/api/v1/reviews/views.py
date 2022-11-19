import django_filters

from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from reviews.models import Category, Genre, Title, Review
from api.v1.reviews.serializers import (CategorySerializer, CommentSerializer,
                                        GenreSerializer, TitleSerializer,
                                        TitlePostSerializer, ReviewSerializer)
from api.v1.users.permissions import IsAdmin, IsAuthorAdminModeratorOrReadOnly, IsOwner


class TitleFilter(django_filters.FilterSet):

    genre = django_filters.CharFilter(field_name='genre__slug')
    category = django_filters.CharFilter(field_name='category__slug')
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = ['name',
                  'year',
                  'genre',
                  'category']


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """Вьюсет для модели Genre."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = ('slug')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Genre, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsAdmin]
        return [permission() for permission in permission_classes]


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """Вьюсет для модели Category."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = ('slug')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Category, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsAdmin]
        return [permission() for permission in permission_classes]


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Title."""
    queryset = Title.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        list = ['create', 'update', 'partial_update']
        if self.action in list:
            return TitlePostSerializer
        return TitleSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsAdmin]
        return [permission() for permission in permission_classes]


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Review."""
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorAdminModeratorOrReadOnly, )

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return super().get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorAdminModeratorOrReadOnly, )

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return (AllowAny(),)
        return super().get_permissions()
