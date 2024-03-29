# Generated by Django 2.2.6 on 2019-10-13 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_donation_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='contact',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='donation',
            name='address',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='donation',
            name='description',
            field=models.CharField(max_length=512),
        ),
    ]
