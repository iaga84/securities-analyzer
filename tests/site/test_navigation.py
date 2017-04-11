# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import pytest


@pytest.mark.django_db
def test_root(django_app):
    res = django_app.get('/')
    assert 'WLD.MI' in res
