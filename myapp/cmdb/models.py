# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
   
    def __str__(self):
        return self.name

class link(models.Model):
    name = models.CharField(max_length=128, unique=True)
    remarks =  models.CharField(max_length=256)
    urls =  models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class device(models.Model):
    hname = models.CharField(max_length=128, unique=True)
    ip  = models.CharField(max_length=64)
    protoclo = models.CharField(max_length=16)
    port = models.CharField(max_length=16)
    uname = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    position = models.CharField(max_length=128)
    remarks = models.CharField(max_length=256)
    state = models.CharField(max_length=8)

    def __str__(self):
        return self.ip
    
