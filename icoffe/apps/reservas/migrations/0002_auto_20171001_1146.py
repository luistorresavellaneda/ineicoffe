# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambientes', '0001_initial'),
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='apellido',
            new_name='apellidos',
        ),
        migrations.AddField(
            model_name='reserva',
            name='detalle',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='mesa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ambientes.Mesa'),
            preserve_default=False,
        ),
    ]