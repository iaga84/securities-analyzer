# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import routers

from s_analyzer.apps.rest.views import SecurityDailyDataViewSet, SecurityDailyMovingAverageViewSet, SecurityViewSet

router = routers.DefaultRouter()
router.register(r'securities', SecurityViewSet)
router.register(r'security_daily_data', SecurityDailyDataViewSet)
router.register(r'security_daily_moving_averages', SecurityDailyMovingAverageViewSet)
