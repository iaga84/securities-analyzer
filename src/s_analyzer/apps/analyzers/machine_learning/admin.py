# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from s_analyzer.apps.analyzers.machine_learning.models import (SecurityDailyMachineLearningPeriod,
                                                               SecurityDailyMachineLearningPrediction,)


@admin.register(SecurityDailyMachineLearningPeriod)
class SecurityDailyMachineLearningPeriodAdmin(admin.ModelAdmin):
    list_display = ('security', 'days')


@admin.register(SecurityDailyMachineLearningPrediction)
class SecurityDailyMachineLearningPredictionAdmin(admin.ModelAdmin):
    list_display = ('period', 'date', 'prediction')
