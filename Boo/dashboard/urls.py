#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from django.conf.urls import include,url
import views





urlpatterns = [
    url(r'/',view=views.index,name="index"),
    url(r'^login/',view=views.login),
]