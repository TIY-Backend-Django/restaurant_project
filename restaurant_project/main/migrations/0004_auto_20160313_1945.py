# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160313_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]
