# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-08 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0007_auto_20171007_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='totalQuestions',
            field=models.IntegerField(default=-1),
        ),
    ]
