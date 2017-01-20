# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-20 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20170118_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoBaterias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baterias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo_baterias', to='principal.Baterias')),
                ('vehiculos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo_items', to='principal.Baterias')),
            ],
            options={
                'verbose_name_plural': 'VehiculosBateriass',
            },
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10)),
                ('m3', models.CharField(max_length=9)),
                ('GrasaChasis', models.CharField(max_length=10)),
                ('SerialCarroceria', models.CharField(max_length=20)),
                ('Color', models.CharField(max_length=20)),
                ('Ano', models.CharField(max_length=20)),
                ('CapacidadCarga', models.CharField(max_length=10)),
                ('MarcaModelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Marcas')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Socios')),
            ],
            options={
                'verbose_name_plural': 'Vehiculoss',
            },
        ),
    ]
