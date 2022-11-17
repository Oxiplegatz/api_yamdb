import csv

from django.core.management.base import BaseCommand

from reviews.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(
                open(csv_file, encoding="utf8"), delimiter=','
            )
            next(dataReader)
            users = []
            for row in dataReader:
                user = User(
                    id=row[0],
                    username=row[1],
                    email=row[2],
                    # role=row[3]
                )
                users.append(user)
            User.objects.bulk_create(users)
