#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password'}))
