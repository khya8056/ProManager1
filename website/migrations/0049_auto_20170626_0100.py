# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-25 19:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0048_uploadmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_log',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
