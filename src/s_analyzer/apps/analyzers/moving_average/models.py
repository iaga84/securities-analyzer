# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from s_analyzer.apps.market_data.models import Security


@python_2_unicode_compatible
class SecurityDailyMovingAveragePeriod(models.Model):
    security = models.ForeignKey(Security, related_name='daily_moving_average_periods')
    days = models.IntegerField()

    class Meta:
        verbose_name_plural = "security daily moving average periods"
        unique_together = ('security', 'days')
        ordering = ['security', 'days']

    def __str__(self):
        return '{} [{} days]'.format(self.security, self.days)


@python_2_unicode_compatible
class SecurityDailyMovingAverage(models.Model):
    date = models.DateField()
    period = models.ForeignKey(SecurityDailyMovingAveragePeriod, related_name='daily_moving_averages')
    average = models.DecimalField(max_digits=12, decimal_places=3)

    class Meta:
        verbose_name_plural = "security daily moving averages"
        unique_together = ('date', 'period')
        ordering = ['date', 'period']

    def __str__(self):
        return '{} [{} days] ({})'.format(self.period.security, self.period.days, self.date)
