# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boo_commander', '0002_auto_20170831_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boo_commander',
            name='methods',
            field=models.CharField(max_length=32),
        ),
    ]
