# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from admin_extra_urls.extras import action, ExtraUrlMixin
from django.contrib import admin

from s_analyzer.apps.analyzers.moving_average.analyzer import refresh_moving_average_records
from s_analyzer.apps.market_data.sync import get_historical_data

from .models import Security, SecurityDailyData


@admin.register(Security)
class SecurityAdmin(ExtraUrlMixin, admin.ModelAdmin):
    @action()
    def refresh(self, request, pk):
        get_historical_data(pk)
        refresh_moving_average_records(pk)


@admin.register(SecurityDailyData)
class SecurityDailyDataAdmin(admin.ModelAdmin):
    pass
