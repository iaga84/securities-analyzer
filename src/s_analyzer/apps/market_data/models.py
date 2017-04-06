# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Security(models.Model):
    symbol = models.CharField(max_length=32, unique=True)
    currency = models.CharField(max_length=32)

    class Meta:
        ordering = ['symbol']

    def __str__(self):
        return '{} ({})'.format(self.symbol, self.currency)


@python_2_unicode_compatible
class SecurityDailyData(models.Model):
    security = models.ForeignKey(Security, related_name='daily_data')
    date = models.DateField()
    opening_price = models.DecimalField(max_digits=12, decimal_places=3)
    highest_price = models.DecimalField(max_digits=12, decimal_places=3)
    lowest_price = models.DecimalField(max_digits=12, decimal_places=3)
    closing_price = models.DecimalField(max_digits=12, decimal_places=3)
    adjusted_closing_price = models.DecimalField(max_digits=12, decimal_places=3)
    volume = models.IntegerField()

    class Meta:
        unique_together = ('security', 'date')
        ordering = ['-date', 'security']

    def __str__(self):
        return '{} ({})'.format(self.security, self.date)
