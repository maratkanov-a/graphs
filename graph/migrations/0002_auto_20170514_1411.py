# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-14 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='_student_friends_+', to='graph.Student', verbose_name='\u0414\u0440\u0443\u0437\u044c\u044f'),
        ),
    ]
