# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import logging
from datetime import datetime, timedelta

from yahoo_finance import Share

from s_analyzer.apps.market_data.models import Security, SecurityDailyData

logger = logging.getLogger(__name__)


def get_historical_data(security_pk, past_days=365):
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
