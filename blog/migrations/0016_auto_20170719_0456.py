# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170719_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='to_date',
            field=models.DateField(blank=True, default=None),
        ),
    ]
