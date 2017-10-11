# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=80)),
                ('last_name', models.CharField(blank=True, max_length=80)),
                ('slug', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='Datetime created')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('points', models.PositiveSmallIntegerField(blank=True)),
                ('created_at', models.DateTimeField(verbose_name='Datetime created')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Student')),
            ],
        ),
    ]
