# Generated by Django 3.2 on 2021-10-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('similMercado', '0004_auto_20211012_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_de_compra',
            field=models.DateField(auto_now_add=True),
        ),
    ]