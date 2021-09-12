# Generated by Django 3.2 on 2021-09-12 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('nuevo', models.BooleanField()),
                ('activo', models.BooleanField()),
                ('id_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='similMercado.categoria')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='similMercado.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_compra', models.DateTimeField(auto_now_add=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='similMercado.producto')),
                ('id_usuario_comprador', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='similMercado.usuario')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='similMercado.vendedor')),
            ],
        ),
    ]
