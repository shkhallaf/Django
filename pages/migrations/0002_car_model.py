# Generated by Django 4.1.1 on 2022-12-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.TextField(default='default'),
        ),
    ]
