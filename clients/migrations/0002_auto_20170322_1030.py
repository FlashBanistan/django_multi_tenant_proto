# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='on_trial',
        ),
        migrations.RemoveField(
            model_name='client',
            name='paid_until',
        ),
    ]
