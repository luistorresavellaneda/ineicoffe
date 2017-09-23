# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0004_remove_producto_imagen'),
        ('ambientes', '0002_mesa_ambiente'),
        ('recursoshumanos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=3, max_digits=7)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('nota', models.TextField(blank=True, default=None, null=True)),
                ('nro_clientes', models.PositiveIntegerField()),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
                ('mesa', models.ManyToManyField(to='ambientes.Mesa')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recursoshumanos.Personal')),
            ],
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.Pedido'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto'),
        ),
    ]