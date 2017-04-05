#!/usr/bin/env python

import codecs
import imp
import os

from setuptools import find_packages, setup

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

app = imp.load_source('s_analyzer', os.path.join(ROOT, 'src', 's_analyzer', '__init__.py'))


def read(*files):
    content = []
    for f in files:
        content.extend(codecs.open(os.path.join(ROOT, 'src', 'requirements', f), 'r').read().split())
    return content


django_requires = read('django.pip')
tests_requires = read('testing.pip')
install_requires = read('install.any.pip')
dev_requires = install_requires + django_requires + tests_requires + read('develop.pip')


setup(name=app.NAME,
      version=app.get_version(),
      url='http://pypi.python.org/pypi/%s/' % app.NAME,
      author='Alessio Iacarelli',
      author_email='iaga84@gmail.com',
      license="MIT License",
      description='Securities Analyzer',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      install_requires=install_requires,
      tests_require=tests_requires,
      extras_require={
          'dev': dev_requires,
          'test': tests_requires,
          'django': django_requires,
      },
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers'
      ]
      )
