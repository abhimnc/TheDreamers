# -*- coding: utf-8 -*-
from django import forms
from uploads.models import Document

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    description = forms.CharField(max_length=255)
    price = forms.IntegerField()
    emailId = forms.CharField(max_length=255)  
    
