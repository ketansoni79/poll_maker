# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-17 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20161217_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
