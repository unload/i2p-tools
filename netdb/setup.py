#!/usr/bin/env python
from distutils.core import setup

setup(name = 'netdb',
    version = '0.0',
    description = 'i2p netdb parser',
    author = 'Jeff Becker, unload',
    author_email = 'ampernand@gmail.com, unload@cryptolab.net',
    url = 'https://github.com/majestrate/i2p-tools',
    package_dir = {'netdb': 'src'},
    packages = ['netdb'],
)
