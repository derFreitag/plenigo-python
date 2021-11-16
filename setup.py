# -*- coding: utf-8 -*-
"""Setuptools configuration file."""
from setuptools import setup
from setuptools import find_packages


short_description = 'Plenigo Python3 SDK'


long_description = '{0}'.format(
    open('README.md').read()
)

print('FIND PACKAGES:')
print(find_packages('plenigo'))

setup(
    name='plenigo-python',
    version='0.0.1',
    description=short_description,
    long_description=long_description,
    # Get more from https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
    ],
    keywords='plenigo',
    author='plenigo',
    author_email='',
    url='',
    license='',
    # packages=find_packages('plenigo'),
    # packages=find_packages(include=("plenigo")),
    # package_dir={'': 'plenigo'},
    # packages=['plenigo'],
    packages=find_packages(),
    # include_package_data=True,
    test_suite='tests',
    zip_safe=False,
    install_requires=['requests'],
    extras_require={'test': ['mock', 'pytest']},
)
