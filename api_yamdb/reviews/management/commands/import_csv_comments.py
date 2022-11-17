import csv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Review, Comment

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(
                open(csv_file, encoding="utf8"), delimiter=','
            )
            next(dataReader)
            comments = []
            for row in dataReader:
                user_id = row[3]
                review_id = row[1]
                user = get_object_or_404(User, id=user_id)
                review = get_object_or_404(Review, id=review_id)
                comment = Comment(
                    id=row[0],
                    text=row[2],
                    pub_date=row[4],
                    review=review,
                    author=user
                )
                comments.append(comment)
            Comment.objects.bulk_create(comments)
