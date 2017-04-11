# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from .default import *  # NOQA

AUTH_PASSWORD_VALIDATORS = []

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
