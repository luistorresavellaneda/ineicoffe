# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursoshumanos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='cargo',
            field=models.PositiveIntegerField(choices=[(1, 'Mozos'), (2, 'Cajero')]),
        ),
    ]