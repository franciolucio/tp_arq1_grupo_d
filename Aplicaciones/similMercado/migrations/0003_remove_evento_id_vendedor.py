# Generated by Django 3.2 on 2021-09-29 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('similMercado', '0002_evento_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='id_vendedor',
        ),
    ]