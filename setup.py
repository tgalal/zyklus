#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import zyklus

setup(
    name='zyklus',
    version=zyklus.__version__,
    url='http://github.com/tgalal/zyklus/',
    license='MIT',
    author='Tarek Galal',
    tests_require=[],
    install_requires = [],
    author_email='tare2.galal@gmail.com',
    description='A simple event loop library',
    #long_description=long_description,
    packages= find_packages(),
    include_package_data=True,
    platforms='any',
    # test_suite='',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        #'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
