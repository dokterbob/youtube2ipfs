#!/usr/bin/env python
import warnings

from setuptools import setup, find_packages

try:
    README = open('README.md').read()
except:
    warnings.warn('Could not read README.md')
    README = None

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    warnings.warn('Could not read requirements.txt')
    REQUIREMENTS = None

setup(
	name='youtube2ipfs',
	version='0.2',
	description='Download videos from YouTube (and similar video platforms) and add them to IPFS.',
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=REQUIREMENTS,
	author='Mathijs de Bruin',
	author_email='mathijs@mathijsfietst.nl',
	url='https://github.com/dokterbob/youtube2ipfs',
	packages=find_packages(),
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: End Users/Desktop',
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: GNU Affero General Public License v3',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.8',
		'Topic :: Utilities'
	],
    entry_points = {
        'console_scripts': ['youtube2ipfs=youtube2ipfs.youtube2ipfs:main'],
    }
)
