# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-09 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipment', '0005_auto_20171009_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_hours_before', models.IntegerField()),
                ('working_hours_after', models.IntegerField()),
                ('work_end_time', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, default='')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment')),
            ],
            options={
                'ordering': ('-work_end_time',),
            },
        ),
    ]
