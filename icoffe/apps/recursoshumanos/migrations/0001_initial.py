# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cargo', models.PositiveIntegerField(choices=[(2, 'Cajero'), (1, 'Mozos')])),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
            },
        ),
    ]