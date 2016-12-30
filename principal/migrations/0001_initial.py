# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-22 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=9, unique=True)),
                ('apellidos', models.CharField(help_text='Maximo 100 caracteres', max_length=100)),
                ('nombres', models.TextField(help_text='Maximo 100 caracteres', max_length=100)),
                ('direccion', models.TextField(help_text='Maximo 200 caracteres', max_length=200)),
                ('telefono1', models.CharField(help_text='Maximo 12 caracteres', max_length=12)),
                ('telefono2', models.CharField(help_text='Maximo 12 caracteres', max_length=12)),
                ('telefono3', models.CharField(help_text='Maximo 12 caracteres', max_length=12)),
                ('correo', models.EmailField(help_text='Maximo 200 caracteres', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Socios',
            },
        ),
    ]
