# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0006_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.CharField(default='conference/base.html', max_length=50),
        ),
    ]
