# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-05 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quizz',
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.CharField(default='galop1', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizz',
            name='level',
            field=models.CharField(default='galop1', max_length=64),
            preserve_default=False,
        ),
    ]