# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patmos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornamn', models.CharField(max_length=255)),
                ('efternamn', models.CharField(max_length=255)),
                ('personnummer', models.CharField(max_length=15)),
                ('adress', models.TextField()),
                ('telefon', models.CharField(max_length=30)),
                ('fodelsedatum', models.CharField(max_length=50)),
                ('dopdatum', models.CharField(max_length=50)),
                ('ankomstdatum', models.CharField(max_length=50)),
                ('avgadatum', models.CharField(max_length=50)),
                ('gift', models.CharField(max_length=7)),
                ('ogift', models.CharField(max_length=7)),
            ],
        ),
    ]