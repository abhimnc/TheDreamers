# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_document_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to='documents/'),
        ),
    ]