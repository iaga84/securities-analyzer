# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import viewsets

from s_analyzer.apps.market_data.models import Security, SecurityDailyData
from s_analyzer.apps.rest.serializers import SecurityDailyDataSerializer, SecuritySerializer


class SecurityViewSet(viewsets.ModelViewSet):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer
    filter_fields = ('symbol', 'currency')


class SecurityDailyDataViewSet(viewsets.ModelViewSet):
    queryset = SecurityDailyData.objects.all()
    serializer_class = SecurityDailyDataSerializer
    filter_fields = ('security', 'date')
