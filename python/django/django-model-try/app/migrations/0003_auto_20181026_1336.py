# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-26 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_timeofsleep_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUsername',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_str', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='timeofsleep',
            name='username',
        ),
    ]