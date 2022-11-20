# Generated by Django 2.2.16 on 2022-11-20 17:09

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True, validators=[reviews.models.validate_year], verbose_name='Год выхода'),
        ),
    ]
