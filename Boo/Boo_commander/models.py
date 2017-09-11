# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


methods = (
    ('GET','GET'),
    ('POST','POST'),
)
class Boo_commander(models.Model):

    id = models.AutoField(primary_key=True) # 自增主键
    work_name = models.CharField(max_length=20) #爬虫名称
    methods = models.CharField(max_length=32) #爬虫爬取方式
    request_url = models.CharField(max_length=1024) #URL里面目前长度匹配1024字节，切记
    request_body = models.CharField(max_length=1024) #POST上传内容
    request_args = models.CharField(max_length=1024) #GET追加参数
    response_timeout = models.IntegerField() #超时时间，手动设置
    response_body = models.CharField(max_length=1024)


    class Meta:
        db_table = 'boo_commander'



