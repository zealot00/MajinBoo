# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django_tables2 import RequestConfig

# Create your views here.
from .forms import New_Boo
from .models import *
from .tables import Boo


def index(request):
    if request.method == 'GET':
        return render(request,template_name='dashboard.html')



def create(request):
    if request.method == 'POST':
        form = New_Boo(request.POST)
        if form.is_valid():
            #这里有个蛋疼的地方，就是这里都不能有空格，这里考虑后期弄个ajax来糊弄过去
            messages.success(request,'添加成功')
            Boo_commander.objects.get_or_create(work_name = form.cleaned_data.get('boo_name'),
                                                methods = form.cleaned_data.get('boo_method'),
                                                request_url = form.cleaned_data.get('boo_url'),
                                                request_body = form.cleaned_data.get('boo_request_body'),
                                                request_args = form.cleaned_data.get('boo_request_args'),
                                                response_timeout = form.cleaned_data.get('boo_request_timeout'),
                                                )
            return HttpResponseRedirect('boo/create_boo')
            #return HttpResponse('ok')
        else:
            return HttpResponse('fail')
    if request.method == 'GET':
        form = New_Boo()
        small = "create new boo"
        return render(request,template_name='boo_add.html',context={'form':form,
                                                                    'small':small},
                      )

def boos(request):
    if request.method == 'GET':
        small = 'view all boos'
        boo_tables = Boo(Boo_commander.objects.all(),)
        RequestConfig(request).configure(boo_tables)
        page_name = '查看爬虫'
        return render(request,template_name='boos.html',context={'small':small,
                                                                 'page_name':page_name,
                                                                 'tables': boo_tables})
