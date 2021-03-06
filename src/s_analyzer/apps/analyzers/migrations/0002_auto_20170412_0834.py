# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 08:34
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market_data', '0002_auto_20170412_0834'),
        ('analyzers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityDailyMovingAverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('average', models.DecimalField(decimal_places=3, max_digits=12)),
            ],
            options={
                'ordering': ['date', 'period'],
                'verbose_name_plural': 'security daily moving averages',
            },
        ),
        migrations.CreateModel(
            name='SecurityDailyMovingAveragePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('security', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_moving_average_periods', to='market_data.Security')),
            ],
            options={
                'ordering': ['security', 'days'],
                'verbose_name_plural': 'security daily moving average periods',
            },
        ),
        migrations.AddField(
            model_name='securitydailymovingaverage',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_moving_averages', to='analyzers.SecurityDailyMovingAveragePeriod'),
        ),
        migrations.AlterUniqueTogether(
            name='securitydailymovingaverageperiod',
            unique_together=set([('security', 'days')]),
        ),
        migrations.AlterUniqueTogether(
            name='securitydailymovingaverage',
            unique_together=set([('date', 'period')]),
        ),
    ]
