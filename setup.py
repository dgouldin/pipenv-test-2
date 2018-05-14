#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pipenv-test-2',
    version='0.1',
    description='Pipenv test 2',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0',
    ],
)
