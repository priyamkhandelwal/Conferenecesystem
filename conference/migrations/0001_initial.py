# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 13:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('confname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgfile', models.FileField(default=None, null=True, upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paperfile', models.FileField(default=None, null=True, upload_to='documents/papers')),
            ],
        ),
        migrations.AddField(
            model_name='conference',
            name='confimages',
            field=models.ManyToManyField(to='conference.Images'),
        ),
        migrations.AddField(
            model_name='conference',
            name='confpapers',
            field=models.ManyToManyField(to='conference.Papers'),
        ),
        migrations.AddField(
            model_name='conference',
            name='editors',
            field=models.ManyToManyField(related_name='_conference_editors_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conference',
            name='manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]