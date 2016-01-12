#!/usr/bin/env python

from setuptools import setup, find_packages

import os

import audiotranscode

setup(
    name='Audiotranscode',
    version=audiotranscode.__version__,
    description='Python module to transcode between audio formats',
    long_description=None,
    author='Pando85',
    author_email='pando855@gmail.com',
    url='https://github.com/pando85/audiotranscode',
    license='GPLv3',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Sound/Audio',
    ],
    zipfile = None,
    tests_require=["nose"],
)