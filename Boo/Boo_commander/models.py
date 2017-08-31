# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Boo_commander(models.Model):

    work_name = models.CharField(max_length=32)