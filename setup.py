# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


install_requires = (
    'requests',
    'requests_toolbelt',
    )
tests_require = (
    )
extras_require = {
    'test': tests_require,
    }
description = "An in-workgroup Connexions batch operations/tranform utility"


setup(
    name='draft-transform-tool',
    version='0.1',
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/connexions/draft-transform-tool",
    license='LGPL, See aslo LICENSE.txt',
    description=description,
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    include_package_data=True,
    entry_points="""\
    [console_scripts]
    draft-transform = drafttransform.cli:main
    """,
    test_suite='drafttransform.tests',
    )
