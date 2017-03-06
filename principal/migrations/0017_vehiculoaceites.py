# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-06 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0016_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoAceites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('aceites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Aceites')),
                ('vehiculos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Vehiculos')),
            ],
        ),
    ]