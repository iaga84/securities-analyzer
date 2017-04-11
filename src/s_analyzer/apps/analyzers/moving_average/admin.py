# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin

from s_analyzer.apps.analyzers.moving_average.models import SecurityDailyMovingAverage, SecurityDailyMovingAveragePeriod


@admin.register(SecurityDailyMovingAverage)
class SecurityDailyMovingAverageAdmin(admin.ModelAdmin):
    list_display = ('period', 'date', 'average')


@admin.register(SecurityDailyMovingAveragePeriod)
class SecurityDailyMovingAveragePeriodAdmin(admin.ModelAdmin):
    pass
