import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Genre, Title, GenreTitle


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(
                open(csv_file, encoding="utf8"), delimiter=','
            )
            next(dataReader)
            genre_titles = []
            for row in dataReader:
                genre_id = row[2]
                title_id = row[1]
                genre = get_object_or_404(Genre, id=genre_id)
                title = get_object_or_404(Title, id=title_id)
                genre_title = GenreTitle(
                    id=row[0],
                    title=title,
                    genre=genre
                )
                genre_titles.append(genre_title)
            GenreTitle.objects.bulk_create(genre_titles)
