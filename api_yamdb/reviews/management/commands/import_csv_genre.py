import csv

from django.core.management.base import BaseCommand

from reviews.models import Genre


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(
                open(csv_file, encoding="utf8"), delimiter=','
            )
            next(dataReader)
            genres = []
            for row in dataReader:
                genre = Genre(
                    id=row[0],
                    name=row[1],
                    slug=row[2]
                )
                genres.append(genre)
            Genre.objects.bulk_create(genres)
