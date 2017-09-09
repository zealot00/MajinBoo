# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect

from .forms import LoginForm
from .models import Systemuser,make_password

# Create your views here.


def index(request):
    hello = 'hello'
    return render(request,template_name='dashboard.html',context={'hello':hello})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Systemuser.objects.get(username=username,password=make_password(password))
            print username
            print password
            print type(user)
            print "done"
            if user is not None:
                #login(request,user)
                request.session['username'] = username
                #url = request.POST.get('source_url','/dashborad')
                return redirect('/')
            #return render(request,template_name='dashboard.html')
        else:
            print "fail"
    else:
        form = LoginForm()

    return render(request, template_name='login.html',context={'form':form})
