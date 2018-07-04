# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 12:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=90)),
                ('password', models.CharField(max_length=16)),
                ('shopintroduct', models.TextField()),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='UserHeader',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='DataDisplay.User')),
                ('url', models.FileField(upload_to='UserHeader')),
            ],
            options={
                'db_table': 'UserHeader',
            },
        ),
    ]
