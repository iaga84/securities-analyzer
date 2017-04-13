# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import logging

import numpy as np
from sklearn.linear_model import ElasticNet

from s_analyzer.apps.analyzers.machine_learning.models import (SecurityDailyMachineLearningPeriod,
                                                               SecurityDailyMachineLearningPrediction,)
from s_analyzer.apps.market_data.models import SecurityDailyData

logger = logging.getLogger(__name__)


def refresh_machine_learning_records(security_pk):
    periods = SecurityDailyMachineLearningPeriod.objects.filter(security__pk=security_pk)

    for period in periods:
        data = []
        target = []

        # machine learning training phase
        logger.info('Machine learning data gathering [{} days]'.format(period.days))
        for entry in SecurityDailyData.objects.filter(security__pk=security_pk):
            latest_days_values = SecurityDailyData.objects.filter(
                security__pk=security_pk,
                date__lt=entry.date).order_by('-date')[:period.days]
            if latest_days_values.count() == period.days:
                current_X = np.array([float(value.adjusted_closing_price) for value in latest_days_values])
                current_y = float(SecurityDailyData.objects.get(
                    security__pk=security_pk,
                    date=entry.date).adjusted_closing_price)

                data.append(current_X)
                target.append(current_y)

        np_data = np.array(data)
        np_target = np.array(target)
        logger.info('Machine learning data gathering  complete [{} days]'.format(period.days))
        elastic_net = ElasticNet()
        elastic_net.fit(np_data, np_target)
        logger.info('Machine learning training complete [{} days / {} values]'.format(period.days, len(data)))

        # machine learning prediction phase
        for entry in SecurityDailyData.objects.filter(security__pk=security_pk):
            latest_days_values = SecurityDailyData.objects.filter(
                security__pk=security_pk,
                date__lt=entry.date).order_by('-date')[:period.days]
            if latest_days_values.count() == period.days:
                current_X = np.array([float(value.adjusted_closing_price) for value in latest_days_values])
                prediction = elastic_net.predict(np.array(current_X).reshape(1, -1))
                SecurityDailyMachineLearningPrediction.objects.update_or_create(
                    period=period, date=entry.date,
                    defaults={
                        'prediction': prediction[0],
                    }
                )
        logger.info('Machine learning predictions completed')
