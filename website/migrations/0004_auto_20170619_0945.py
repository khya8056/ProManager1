# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170619_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='work',
        ),
        migrations.AddField(
            model_name='work',
            name='t_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='website.teams'),
        ),
    ]