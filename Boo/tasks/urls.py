#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'


from django.conf.urls import include,url
import views





urlpatterns = [
    url(r'^$',view=views.index,),
    url(r'^create_task/',view=views.create,),
    url(r'^task/',view=views.tasks,),
    #url(r'/login',view=views.login,name="login"),
]