# Generated by Django 4.0.3 on 2022-03-24 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_sell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sell',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
