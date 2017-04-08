# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from datetime import datetime, timedelta

from yahoo_finance import Share

from s_analyzer.apps.market_data.models import Security, SecurityDailyData


def get_historical_data(security_pk, past_days=360):
    security = Security.objects.get(pk=security_pk)

    yahoo = Share(security.symbol)

    start_date = datetime.today() - timedelta(days=past_days)
    today = datetime.today()

    history = yahoo.get_historical(start_date.strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d'))

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
