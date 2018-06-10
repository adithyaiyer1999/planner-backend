# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-10 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('password', models.CharField(max_length=400)),
                ('email_id', models.EmailField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='joiningTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfJoining', models.DateField(verbose_name=b'date set')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.customer')),
            ],
        ),
        migrations.CreateModel(
            name='taskDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=1000)),
                ('taskDate', models.DateField(verbose_name=b'date set')),
                ('taskTime', models.TimeField(verbose_name=b'time set')),
                ('location', models.CharField(max_length=1000)),
                ('customersInvolved', models.ManyToManyField(through='tasks.joiningTask', to='tasks.customer')),
            ],
        ),
        migrations.AddField(
            model_name='joiningtask',
            name='taskDetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.taskDetails'),
        ),
    ]
