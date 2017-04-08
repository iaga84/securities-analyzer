# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import serializers

from s_analyzer.apps.market_data.models import Security, SecurityDailyData


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'


class SecurityDailyDataSerializer(serializers.ModelSerializer):
    security = SecuritySerializer()

    class Meta:
        model = SecurityDailyData
        fields = '__all__'
