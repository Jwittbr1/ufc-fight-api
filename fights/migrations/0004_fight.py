# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-20 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fights', '0003_auto_20160620_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner_name', models.CharField(max_length=255)),
                ('winner_url', models.CharField(max_length=255)),
                ('loser_name', models.CharField(max_length=255)),
                ('loser_url', models.CharField(max_length=255)),
                ('method', models.CharField(max_length=255)),
                ('referee', models.CharField(max_length=255)),
                ('round', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('loser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='losing', to='fights.Fighter')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning', to='fights.Fighter')),
            ],
        ),
    ]