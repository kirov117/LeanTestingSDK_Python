from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name = 'LeanTestingSDK',

	version = '1.0.0',

	description = 'Lean Testing Python Client Library',
	long_description = long_description,

	url = 'https://github.com/kirov117/LeanTestingSDK_Python',

	author = 'Marcel Bontaș',
	author_email = 'marcel.bontas@yandex.ru',

	license = 'Proprietary',

	classifiers = [
		'Development Status :: 5 - Production/Stable',

		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',

		'License :: Other/Proprietary License',

		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
	],

	keywords = 'development',

	# packages = find_packages(exclude = ['tests']),
	packages = find_packages(),

	install_requires = ['pycurl'],

	extras_require = {
		'test': ['unittest2']
	},

	include_package_data = True
)
