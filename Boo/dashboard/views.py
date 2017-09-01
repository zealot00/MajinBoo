# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    #return render(request,template_name='index.html')
    return render(request,template_name='dashboard.html')


def login(request):
    return render(request,template_name='login.html')
