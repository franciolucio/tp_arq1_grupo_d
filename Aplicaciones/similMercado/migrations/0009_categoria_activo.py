# Generated by Django 3.2 on 2021-10-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('similMercado', '0008_auto_20211019_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
