# Generated by Django 2.2.6 on 2019-10-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_points',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
