# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import logging
from datetime import datetime, timedelta

from django.db.models import Avg
from yahoo_finance import Share

from s_analyzer.apps.market_data.models import (Security, SecurityDailyData, SecurityDailyMovingAverage,
                                                SecurityDailyMovingAveragePeriod, )

logger = logging.getLogger(__name__)


def get_historical_data(security_pk, past_days=360):
    start_date = datetime.today() - timedelta(days=past_days)
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    security = Security.objects.get(pk=security_pk)

    if not SecurityDailyData.objects.filter(security__pk=security_pk, date=yesterday).exists():
        logger.info('fetching latest {} days of data about {} from yahoo...'.format(past_days, security))
        yahoo = Share(security.symbol)
        history = yahoo.get_historical(start_date.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d'))
        logger.info('fetching completed, now saving data...')

        for record in history:
            SecurityDailyData.objects.update_or_create(
                security=security, date=record['Date'],
                defaults={'opening_price': record['Open'],
                          'highest_price': record['High'],
                          'lowest_price': record['Low'],
                          'closing_price': record['Close'],
                          'adjusted_closing_price': record['Adj_Close'],
                          'volume': record['Volume']
                          },
            )
        logger.info('historical data saved')
    else:
        logger.info('skipping fetching data about {}'.format(security))


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


def refresh_moving_average_records(security_pk, past_days=31):
    start_date = datetime.today() - timedelta(days=past_days)

    for date in (start_date + timedelta(n) for n in range(past_days)):
        refresh_moving_average_single_record(security_pk, date)
