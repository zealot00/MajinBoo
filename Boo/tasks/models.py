# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=32) #任务名称
    task_type = models.CharField(max_length=32) #任务类型
    active = models.BooleanField(default=True) # 是否激活，默认是
    loop_max = models.IntegerField(max_length=9) #任务循环次数
    job_id = models.CharField(max_length=32) #任务ID

    class Meta:
        db_table = 'tasks'



class Task_logs(models.Model):
    id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Tasks)
    create_time = models.DateTimeField()
    end_time = models.DateTimeField()
    task_status = models.CharField(max_length=9,default='waiting')

    class Meta:
        db_table = 'task_logs'