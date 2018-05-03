#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def readme():
    with open('README.md') as readme_file:
        return readme_file.read()

setup(
    name = 'rabbithat',
    version = '1.0.1',
    description = 'rabbithat - code management for Snippet',
    long_description=readme(),
    download_url = 'https://github.com/dellielo/dellielo',
    url = 'https://github.com/dellielo/dellielo',
    author = 'Elodie Dellier',
    author_email = 'dellielo03@gmail.com',
    packages = ['rabbithat'],
    license = "MIT",
    packages=find_packages(),
    install_requires = [],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        ],
    entry_points='''
        
    ''',
    )
