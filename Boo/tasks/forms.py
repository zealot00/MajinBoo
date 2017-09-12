#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'


from django import forms
from .models import Tasks,Task_logs



class New_tasks(forms.Form):
    task_name = forms.CharField(max_length=32,label='任务名称') #
    task_type = forms.ChoiceField(label='任务类型')  #TODO: 需要增加类型映射，可以在models里面增加集合
    active = forms.BooleanField(label='是否激活')
    loop_max = forms.IntegerField(label='循环次数')

