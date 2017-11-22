# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=128, null=True)),
                ('phone', models.CharField(max_length=128, null=True)),
                ('note', models.TextField()),
            ],
        ),
    ]
