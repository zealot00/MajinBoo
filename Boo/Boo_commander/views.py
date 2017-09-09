# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from .forms import New_Boo


def index(request):
    if request.method == 'GET':
        return render(request,template_name='dashboard.html')



def create(request):
    if request.method == 'POST':
        form = New_Boo(request.POST)
        if form.is_valid():
            print form.cleaned_data['boo_name']
            return HttpResponseRedirect('boo/create_boo/')
    if request.method == 'GET':
        form = New_Boo()
        return render(request,template_name='dashboard.html',context={'form':form})