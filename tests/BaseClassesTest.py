import sys
import os

import unittest2 as unittest

# adds current SDK path to sys.path for imports
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../LeanTestingSDK'))

from PyClient import PyClient

from Exception.SDKInvalidArgException import SDKInvalidArgException

from BaseClass.Entity import Entity
from BaseClass.EntityHandler import EntityHandler

class BaseClassesTest(unittest.TestCase):

	# Entity
	def testEntityDefined(self):
		Entity

	def testEntityDataParsing(self):
		data = {'id': 1}
		entity = Entity(PyClient(), data)
		self.assertIs(entity.data, data)

	def testEntityInstanceNonArrData(self):
		self.assertRaises(SDKInvalidArgException, Entity, PyClient(), '')
	def testEntityInstanceEmptyData(self):
		self.assertRaises(SDKInvalidArgException, Entity, PyClient(), {})
	# END Entity



	# EntityHandler
	def testEntityHandlerDefined(self):
		EntityHandler

	def testEntityHandlerCreateNonArrFields(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.create, '')
	def testEntityHandlerCreateEmptyFields(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.create, {})

	def testEntityHandlerAllNonArrFilters(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.all, '')
	def testEntityHandlerAllInvalidFilters(self):
		h = EntityHandler(PyClient())
		self.assertRaisesRegex(SDKInvalidArgException, 'XXXfilterXXX', h.all, {'XXXfilterXXX': 9999})
	def testEntityHandlerAllSupportedFilters(self):
		EntityHandler(PyClient()).all({'include': ''})
		EntityHandler(PyClient()).all({'limit': 10})
		EntityHandler(PyClient()).all({'page': 2})

	def testEntityHandlerFindNonIntID(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.find, '')

	def testEntityHandlerDeleteNonIntID(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.delete, '')

	def testEntityHandlerUpdateNonIntID(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.update, '', {'x': 5})
	def testEntityHandlerUpdateNonArrFields(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.update, 5, '')
	def testEntityHandlerUpdateEmptyFields(self):
		h = EntityHandler(PyClient())
		self.assertRaises(SDKInvalidArgException, h.update, 5, {})
	# END EntityHandler


if __name__ == '__main__':
	unittest.main()
