# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-03 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='serial_no',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]