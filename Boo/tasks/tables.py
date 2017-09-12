#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'


import django_tables2 as tables
from .models import Tasks,Task_logs


class Tasks_table(tables.Table):
    class Meta:
        model = Tasks
        attrs = {'class' : 'paleblue'}



class Tasks_log(tables.Table):
    class Meta:
        model = Task_logs
        attrs = {'class' : 'paleblue'}