# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "s_analyzer.settings.default")

application = get_wsgi_application()
