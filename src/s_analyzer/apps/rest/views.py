# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import viewsets

from s_analyzer.apps.analyzers.machine_learning.models import SecurityDailyMachineLearningPrediction
from s_analyzer.apps.analyzers.moving_average.models import SecurityDailyMovingAverage
from s_analyzer.apps.market_data.models import Security, SecurityDailyData
from s_analyzer.apps.rest.serializers import (SecurityDailyDataLiteSerializer, SecurityDailyDataSerializer,
                                              SecurityDailyMachineLearningPredictionLiteSerializer,
                                              SecurityDailyMachineLearningPredictionSerializer,
                                              SecurityDailyMovingAverageLiteSerializer,
                                              SecurityDailyMovingAverageSerializer, SecuritySerializer,)


class BaseModelViewSet(viewsets.ModelViewSet):
    additional_serializers = {}

    def get_serializer_class(self):
        return self.additional_serializers.get(self.request.GET.get('serializer', None),
                                               self.serializer_class)


class SecurityViewSet(BaseModelViewSet):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer
    filter_fields = ('symbol', 'currency')


class SecurityDailyDataViewSet(BaseModelViewSet):
    queryset = SecurityDailyData.objects.all()
    serializer_class = SecurityDailyDataSerializer
    additional_serializers = {
        'lite': SecurityDailyDataLiteSerializer
    }
    filter_fields = ('security', 'security__symbol', 'date')


class SecurityDailyMovingAverageViewSet(BaseModelViewSet):
    queryset = SecurityDailyMovingAverage.objects.all()
    serializer_class = SecurityDailyMovingAverageSerializer
    additional_serializers = {
        'lite': SecurityDailyMovingAverageLiteSerializer
    }
    filter_fields = ('period', 'period__days', 'period__security', 'period__security__symbol', 'date')


class SecurityDailyMachineLearningPredictionViewSet(BaseModelViewSet):
    queryset = SecurityDailyMachineLearningPrediction.objects.all()
    serializer_class = SecurityDailyMachineLearningPredictionSerializer
    additional_serializers = {
        'lite': SecurityDailyMachineLearningPredictionLiteSerializer
    }
    filter_fields = ('period', 'period__days', 'period__security', 'period__security__symbol', 'date')
