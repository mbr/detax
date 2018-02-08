#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    buf = open(os.path.join(os.path.dirname(__file__), fname), 'rb').read()
    return buf.decode('utf8')


setup(
    name='detax',
    version='0.1',
    description='German income tax library',
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='https://github.com/mbr/detax',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'detax = detax.cli:cli',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ])
