# -*- coding: utf-8 -*-
from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0)
    emailId = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description
    

    

 

