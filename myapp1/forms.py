# -*- coding: utf-8 -*-
from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    description = forms.CharField(max_length=255)

    emailId = forms.CharField(max_length=255)  
    
