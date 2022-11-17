import csv

from django.core.management.base import BaseCommand

from reviews.models import Category


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(
                open(csv_file, encoding="utf8"), delimiter=','
            )
            next(dataReader)
            categories = []
            for row in dataReader:
                category = Category(
                    id=row[0],
                    name=row[1],
                    slug=row[2]
                )
                categories.append(category)
            Category.objects.bulk_create(categories)
