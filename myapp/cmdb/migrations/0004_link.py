# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-28 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('remarks', models.CharField(max_length=256)),
                ('urls', models.CharField(max_length=256)),
            ],
        ),
    ]
