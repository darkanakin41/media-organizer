#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import os
import re

from setuptools import setup, find_packages

folder = 'organizer'
project_name = 'media-organizer'
executable = 'media-organizer'

here = os.path.abspath(os.path.dirname(__file__))
history = ""

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

if os.path.exists(os.path.join(here, 'CHANGELOG.md')):
    with io.open(os.path.join(here, 'CHANGELOG.md'), encoding='utf-8') as f:
        history = f.read()
project_dir = os.path.dirname(os.path.realpath(__file__))

requirements = os.path.join(project_dir, 'requirements.txt')
requirements_dev = os.path.join(project_dir, 'requirements-dev.txt')

with open(requirements) as f:
    install_requires = list(map(str.strip, f.read().splitlines()))[1:]

with open(requirements_dev) as f:
    dev_require = list(filter(lambda x: not x.startswith('https://'), map(str.strip, f.read().splitlines())))[:-1]

dependency_link_pattern = re.compile("(\S+:\/\/\S+)#egg=(\S+)")

dependency_links = []
install_requires_fixed = []
for req in install_requires:
    match = dependency_link_pattern.match(req)
    if match:
        install_requires_fixed.append(match.group(2))
        dependency_links.append(match.group(1))
    else:
        install_requires_fixed.append(req)
install_requires = install_requires_fixed

package_data = []

entry_points = {
    'console_scripts': [
        '{} = {}.__main__:main'.format(executable, folder)
    ]
}

with io.open('{}/__version__.py'.format(folder), 'r') as f:
    version = re.search(r'^__version__\st*=\s*[\'"]([^\'"]*)[\'"]$', f.read(), re.MULTILINE).group(1)

args = dict(name='darkanakin41-{}'.format(project_name),
            version=version,
            description='{} - A set of tools for media organisation !'.format(project_name),
            long_description=readme + '\n' * 2 + history,
            long_description_content_type='text/markdown',
            # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
            classifiers=['Development Status :: 5 - Production/Stable',
                         'License :: OSI Approved :: MIT License',
                         'Operating System :: OS Independent',
                         'Intended Audience :: Developers',
                         'Programming Language :: Python :: 3.8',
                         'Topic :: Software Development :: Libraries :: Python Modules'
                         ],
            keywords='media organizer media-organizer',
            author='Pierre LEJEUNE',
            author_email='darkanakin41@gmail.com',
            url='https://github.com/darkanakin41/{}'.format(project_name),
            license='MIT',
            packages=find_packages(),
            include_package_data=True,
            install_requires=install_requires,
            dependency_links=dependency_links,
            entry_points=entry_points,
            zip_safe=True,
            extras_require={
                'dev': dev_require
            })

setup(**args)
