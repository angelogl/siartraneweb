# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-30 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_baterias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cauchos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cauchoss',
            },
        ),
    ]
