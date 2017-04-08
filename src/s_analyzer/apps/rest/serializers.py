# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import serializers

from s_analyzer.apps.market_data.models import (Security, SecurityDailyData, SecurityDailyMovingAverage,
                                                SecurityDailyMovingAveragePeriod,)


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'


class SecurityDailyDataSerializer(serializers.ModelSerializer):
    security = SecuritySerializer()

    class Meta:
        model = SecurityDailyData
        fields = '__all__'


class SecurityDailyDataLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityDailyData
        fields = '__all__'

    def to_representation(self, obj):
        return int(obj.date.strftime("%s")) * 1000, obj.adjusted_closing_price


class SecurityDailyMovingAveragePeriodSerializer(serializers.ModelSerializer):
    security = SecuritySerializer()

    class Meta:
        model = SecurityDailyMovingAveragePeriod
        fields = '__all__'


class SecurityDailyMovingAverageSerializer(serializers.ModelSerializer):
    period = SecurityDailyMovingAveragePeriodSerializer()

    class Meta:
        model = SecurityDailyMovingAverage
        fields = '__all__'


class SecurityDailyMovingAverageLiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityDailyMovingAverage
        fields = '__all__'

    def to_representation(self, obj):
        return int(obj.date.strftime("%s")) * 1000, obj.average
