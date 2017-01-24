# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_cooperativas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cooperativas',
            options={'verbose_name_plural': 'Cooperativass'},
        ),
        migrations.AddField(
            model_name='socios',
            name='cooperativa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='principal.Cooperativas'),
            preserve_default=False,
        ),
    ]