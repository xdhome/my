# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WYKL', '0003_auto_20181101_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgpath', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'nav',
            },
        ),
    ]