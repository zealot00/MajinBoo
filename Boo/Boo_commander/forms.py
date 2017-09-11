#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from django import forms
from .models import methods



class New_Boo(forms.Form):
    boo_name = forms.CharField(max_length=100,label='爬虫名称',empty_value='名称不能为空',error_messages={'required':"名称不能为空"})
    boo_method = forms.ChoiceField(choices=methods,label='爬取方式')
    boo_url = forms.CharField(max_length=255,label='爬取地址')
    boo_request_args = forms.CharField(max_length=255,label='爬取参数',required=False,initial='')
    boo_request_body = forms.CharField(max_length=255,label='提交内容',required=False,initial='')
    boo_request_timeout = forms.IntegerField(min_value=1,max_value=10,label='爬取超时')

