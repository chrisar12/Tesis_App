# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-20 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SituacionSalud', '0013_auto_20171219_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situacionsalud',
            name='edad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SituacionSalud.Edad'),
        ),
    ]
