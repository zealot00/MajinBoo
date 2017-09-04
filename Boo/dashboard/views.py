# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect

from .forms import LoginForm

# Create your views here.


def index(request):
    #return render(request,template_name='index.html')
    return render(request,template_name='dashboard.html')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print "done"
            return render(request,template_name='dashboard.html')
    else:
        form = LoginForm()

    #return render(request, template_name='login.html',{ 'form':form })
    return render(request, template_name='login.html')
