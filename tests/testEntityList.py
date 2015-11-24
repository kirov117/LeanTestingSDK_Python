import sys
import os

import unittest2 as unittest
from unittest.mock import MagicMock

# adds current SDK path to sys.path for imports
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../LeanTestingSDK'))

from PyClient import PyClient

from Exception.SDKUnexpectedResponseException import SDKUnexpectedResponseException

from BaseClass.APIRequest import APIRequest
from BaseClass.EntityList import EntityList

class EntityListTest(unittest.TestCase):

	def testEntityListDefined(self):
		EntityList



	def testEntityListBadRespMissingMeta(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : '{"x": []}', 'status' : 200})

		self.assertRaisesRegex(SDKUnexpectedResponseException, 'meta', EntityList, PyClient(), req, 'X')
	def testEntityListBadRespMissingMetaPagination(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : '{"x": [], "meta": {}}', 'status' : 200})

		self.assertRaisesRegex(SDKUnexpectedResponseException, 'pagination', EntityList, PyClient(), req, 'X')
	def testEntityListBadRespMissingCollection(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : '{"meta": {"pagination": {}}}', 'status' : 200})

		self.assertRaisesRegex(SDKUnexpectedResponseException, 'collection', EntityList, PyClient(), req, 'X')
	def testEntityListBadRespMultipleCollections(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : '{"xxy": [], "yyx": [], "meta": {"pagination": {}}}', 'status' : 200})

		self.assertRaisesRegex(SDKUnexpectedResponseException, 'multiple', EntityList, PyClient(), req, 'X')


if __name__ == '__main__':
	unittest.main()
