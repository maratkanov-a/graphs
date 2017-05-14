# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-14 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.IntegerField(choices=[(0, '\u041e\u0442\u043b\u0438\u0447\u043d\u0438\u043a\u0438'), (1, '\u0425\u043e\u0440\u043e\u0448\u0438\u0441\u0442\u044b'), (2, '\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0438'), (3, '\u0414\u0432\u043e\u0435\u0447\u043d\u0438\u043a\u0438'), (4, '\u041f\u0440\u043e\u0433\u0443\u043b\u044c\u0449\u0438\u043a\u0438')], verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430')),
                ('friends', models.ManyToManyField(related_name='_student_friends_+', to='graph.Student', verbose_name='\u0414\u0440\u0443\u0437\u044c\u044f')),
            ],
        ),
    ]