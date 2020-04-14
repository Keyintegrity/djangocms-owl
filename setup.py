#!/usr/bin/env python

import os
import sys

import djangocms_owl

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_owl.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='djangocms-owl',
    version=version,
    description="""Djangocms plugin for owl carousel v1""",
    long_description=readme,
    author='Digital Anvil Ltd',
    author_email='webmaster@digitalanvil.co.uk',
    url='https://github.com/digital-anvil/djangocms-owl',
    packages=[
        'djangocms_owl',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.11,<3.0',
        'django-cms>=3.2.3,<4.0',
        'django-appconf>=1.0.1,<2.0',
        'jsonfield>=2.1,<4.0',
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangocms-owl',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
