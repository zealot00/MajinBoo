# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boo_commander',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=20)),
                ('methods', models.CharField(max_length=1)),
                ('request_url', models.CharField(max_length=1024)),
                ('request_body', models.CharField(max_length=1024)),
                ('request_args', models.CharField(max_length=1024)),
                ('response_timeout', models.IntegerField()),
                ('response_body', models.CharField(max_length=1024)),
            ],
        ),
    ]
