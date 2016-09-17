# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=600)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('location', models.CharField(max_length=200)),
                ('taken', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateTimeField(verbose_name='birthdate')),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='owner',
            field=models.ForeignKey(to='homepage.User'),
        ),
    ]
