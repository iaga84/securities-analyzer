# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os

import vcr


def get_vcr(**kwargs):
    defaults = dict(serializer='json',
                    cassette_library_dir='cassettes',
                    record_mode='once',
                    match_on=['uri', 'method'],
                    filter_headers=['authorization'],
                    filter_post_data_parameters=['username', 'password'])
    defaults.update(kwargs)
    return vcr.VCR(**defaults)


def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 's_analyzer.settings.testing')

    import django
    django.setup()
