#!/usr/bin/env python

from distutils.core import setup

setup(name='forecaster',
      version='1.0',
      description='Forecaster uses a probabilistic mass-radius relation as the underlying model. '
                  'It can forecast mass (radius) given radius (mass) measurements.',
      author='Jingjing Chen, David M. Kipping',
      packages=['numpy', 'scipy', 'h5py'],
     )