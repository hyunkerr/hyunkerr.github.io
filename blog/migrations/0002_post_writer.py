# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-31 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.TextField(default=''),
        ),
    ]
