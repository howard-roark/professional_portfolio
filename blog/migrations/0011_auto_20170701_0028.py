# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170625_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinterest',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='professionalinterest',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
