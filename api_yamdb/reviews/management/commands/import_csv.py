import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import (
    Category, Genre, GenreTitle, Title, Review, Comment
)
from users.models import CustomUser

MODELS_FILES = {
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    GenreTitle: 'genre_title.csv',
    CustomUser: 'users.csv',
    Review: 'review.csv',
    Comment: 'comments.csv'
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model, file_name in MODELS_FILES.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{file_name}', encoding="utf8"
            ) as csv_file:
                dataReader = csv.DictReader(csv_file, delimiter=',')
                items = []
                for row in dataReader:
                    for mod in MODELS_FILES.keys():
                        mod_name = mod.__name__.lower()
                        for field, value in row.items():
                            if mod_name == field or (
                                mod_name == 'customuser' and field == 'author'
                            ):
                                row[field] = get_object_or_404(mod, id=value)
                    item = model(**row)
                    items.append(item)
                model.objects.bulk_create(items)
