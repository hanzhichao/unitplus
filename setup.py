#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="unittest enhancement",
    entry_points={
        'console_scripts': [
            'unitplus=unitplus.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    # long_description=readme + '\n\n' + history,
    # long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='unitplus',
    name='unitplus',
    packages=find_packages(include=['unitplus', 'unitplus.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hanzhichao/unitplus',
    version='0.1.0',
    zip_safe=False,
)
