import datetime as dt

from django.db.models import Avg, IntegerField

from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Title, Review
from rest_framework.validators import UniqueTogetherValidator


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Genre."""

    class Meta:
        fields = ('name', 'slug')
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Category."""

    class Meta:
        fields = ('name', 'slug')
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Title."""
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
        model = Title

    def get_rating(self, obj):
        return obj.reviews.aggregate(
            Avg('score', output_field=IntegerField())
        )['score__avg']

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год выхода!')
        return value


class TitlePostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Title
    для создания и редактирования произведения.
    """
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('author', 'title',)
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'pub_date']
