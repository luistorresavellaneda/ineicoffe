# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('nro_personas', models.PositiveIntegerField(default=1, help_text='Debe incluir a las personas')),
                ('fecha', models.DateTimeField()),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
