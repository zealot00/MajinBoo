#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=32)
