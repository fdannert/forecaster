#!/usr/bin/env python

from setuptools import setup

setup(
    name='forecaster',
    version='0.1',
    packages=['forecaster'],
    include_package_data=True,
    install_requires=['numpy',
                      'scipy',
                      'h5py']
)