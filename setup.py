# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
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
		'Development Status :: 5 - Production',

		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',

		'License :: Proprietary License',

		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
	],

	keywords = 'development',

	packages = find_packages(exclude = ['contrib', 'docs', 'tests']),

	install_requires = [],

	# List additional groups of dependencies here (e.g. development
	# dependencies). You can install these using the following syntax,
	# for example:
	# $ pip install -e .[dev,test]
	# extras_require = {
	# 	'dev': ['check-manifest'],
	# 	'test': ['coverage'],
	# },

	# package_data = {
	# 	'sample': ['package_data.dat'],
	# },

	# Although 'package_data' is the preferred approach, in some case you may
	# need to place data files outside of your packages. See:
	# http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
	# In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
	# data_files = [('my_data', ['data/data_file'])],

	# entry_points = {
	# 	'console_scripts': [
	# 		'sample=sample:main',
	# 	],
	# },
)
