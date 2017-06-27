# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0007_auto_20170619_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Team Member', 'TM'), ('Team Leader', 'TL'), ('Project Manager', 'PM')], max_length=250)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.projects')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='team_member',
            old_name='s_id',
            new_name='mem_id',
        ),
        migrations.RemoveField(
            model_name='main_admin',
            name='a_id',
        ),
        migrations.AddField(
            model_name='role',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.student'),
        ),
    ]