import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Title, Category


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(
                open(csv_file, encoding="utf8"), delimiter=','
            )
            next(dataReader)
            titles = []
            for row in dataReader:
                category_id = row[3]
                category = get_object_or_404(Category, id=category_id)
                title = Title(
                    id=row[0],
                    name=row[1],
                    year=row[2],
                    category=category
                )
                titles.append(title)
            Title.objects.bulk_create(titles)
