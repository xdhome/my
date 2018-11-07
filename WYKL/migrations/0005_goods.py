# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WYKL', '0004_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsid', models.CharField(max_length=5)),
                ('goodsimg', models.CharField(max_length=100)),
                ('goodsname', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('descript', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'goods',
            },
        ),
    ]