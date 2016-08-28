# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0003_userprofile_regconf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pic',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userlogin.ProfilePic'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='usertype',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
