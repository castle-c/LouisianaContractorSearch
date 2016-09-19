# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0002_auto_20160916_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompaniesByParish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=55)),
                ('company_name', models.CharField(max_length=55)),
                ('state', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'CompaniesByParish',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=55)),
                ('owner', models.CharField(max_length=55)),
                ('company_id', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=55)),
                ('address', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('zipcode', models.CharField(max_length=55)),
                ('phone', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'CompanyInfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parish_name', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'Parish',
                'managed': False,
            },
        ),
    ]
