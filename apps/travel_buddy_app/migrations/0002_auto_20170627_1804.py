# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-27 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_and_registration_app', '0002_auto_20170627_1656'),
        ('travel_buddy_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator_trips', to='login_and_registration_app.User'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='users',
            field=models.ManyToManyField(related_name='trips', to='login_and_registration_app.User'),
        ),
    ]
