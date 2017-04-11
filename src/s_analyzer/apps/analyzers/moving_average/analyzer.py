# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import logging
from datetime import datetime, timedelta

from django.db.models import Avg

from s_analyzer.apps.analyzers.moving_average.models import SecurityDailyMovingAverage, SecurityDailyMovingAveragePeriod
from s_analyzer.apps.market_data.models import Security, SecurityDailyData

logger = logging.getLogger(__name__)


def refresh_moving_average_single_record(security_pk, today):
    security = Security.objects.get(pk=security_pk)
    periods = SecurityDailyMovingAveragePeriod.objects.filter(security__pk=security_pk)

    for period in periods:
        historical_values = SecurityDailyData.objects.filter(
            security__pk=security_pk,
            date__lt=today
        ).order_by('-date')[:period.days]
        if historical_values.count() < period.days:
            logger.info(
                'not enough items to calculate moving average [{}] for {} ({})'.format(period.days, security,
                                                                                       today.strftime('%Y-%m-%d')))
        else:
            assert historical_values.count() == period.days
            avg = historical_values.aggregate(Avg('adjusted_closing_price'))['adjusted_closing_price__avg']

            SecurityDailyMovingAverage.objects.update_or_create(
                period=period, date=today,
                defaults={
                    'average': avg,
                },
            )
            logger.info(
                'set moving average [{}] for {} ({}) to {}'.format(period.days, security, today.strftime('%Y-%m-%d'),
                                                                   avg))


def refresh_moving_average_records(security_pk, past_days=365):
    start_date = datetime.today() - timedelta(days=past_days)

    for date in (start_date + timedelta(n) for n in range(past_days)):
        refresh_moving_average_single_record(security_pk, date)
