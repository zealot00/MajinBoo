#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'


import django_tables2 as tables
from .models import Boo_commander


class Boo(tables.Table):
    class Meta:
        model = Boo_commander
        #attrs = {'class' : 'paleblue','table':'border cellpadding=10'}
        attrs = {'class' : 'paleblue',
                 'cellpadding' : 10,
                 'align' : 'left',
                         'td' :{
                         'align' :'center'
                         }
                 }
