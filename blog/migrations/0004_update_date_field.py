# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-19 05:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_time_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
