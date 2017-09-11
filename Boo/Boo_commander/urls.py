#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'


from django.conf.urls import include,url
import views





urlpatterns = [
    url(r'^$',view=views.index,),
    url(r'^dashborad/',view=views.index,),
    url(r'^create_boo/',view=views.create,),
    url(r'^boo/',view=views.boos,),
    #url(r'/login',view=views.login,name="login"),
]