# -*- coding: utf-8 -*-

import hashlib,types
#from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tasks(models.Model):

    task_id = models.IntegerField()
    task_name = models.CharField(max_length=32)


    def __str__(self):
        return self.task_name

    class Meta:
         db_table = "tasks"


class Systemuser(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def make_password(self,password):
        try:
            if types(password) is types.StringType:
                md5 = hashlib.md5()
                salt = "wocaonidaye"
                md5.update(password+salt)
                md5_password = md5.hexdigest()
                md5.update(md5_password)
                md5_password_f = md5.hexdigest()
                return md5_password_f
        except Exception,e:
            return False

    class Meta:
        db_table = "systemuser"


