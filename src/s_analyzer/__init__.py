# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

NAME = 'securities-analyzer'
VERSION = __version__ = (0, 1, 0, 'alpha', 0)
__author__ = 'Alessio Iacarelli'


def get_version():
    assert len(VERSION) == 5
    assert VERSION[3] in ('alpha', 'beta', 'rc', 'final')

    parts = 2 if VERSION[2] == 0 else 3
    main = '.'.join(str(x) for x in VERSION[:parts])

    return main
