import sys
import os

import unittest2 as unittest
from unittest.mock import MagicMock

# adds current SDK path to sys.path for imports
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../LeanTestingSDK'))

from PyClient import PyClient

from Exception.SDKInvalidArgException			import SDKInvalidArgException
from Exception.SDKBadJSONResponseException		import SDKBadJSONResponseException
from Exception.SDKErrorResponseException		import SDKErrorResponseException
from Exception.SDKUnexpectedResponseException	import SDKUnexpectedResponseException

from BaseClass.APIRequest import APIRequest

class APIRequestTest(unittest.TestCase):

	def testAPIRequestDefined(self):
		APIRequest




	def testAPIRequestInstanceNonStrEndpoint(self):
		self.assertRaises(SDKInvalidArgException, APIRequest, PyClient(), 12751, 'GET')
	def testAPIRequestInstanceNonStrMethod(self):
		self.assertRaises(SDKInvalidArgException, APIRequest, PyClient(), '/', 1233)
	def testAPIRequestInstanceSupportedMethod(self):
		APIRequest(PyClient(), '/', 'GET')
		APIRequest(PyClient(), '/', 'POST')
		APIRequest(PyClient(), '/', 'PUT')
		APIRequest(PyClient(), '/', 'DELETE')
	def testAPIRequestInstanceNonSupportedMethod(self):
		self.assertRaises(SDKInvalidArgException, APIRequest, PyClient(), '/', 'XXX')
	def testAPIRequestInstanceNonArrOpts(self):
		self.assertRaises(SDKInvalidArgException, APIRequest, PyClient(), '/', 'GET', 12123)
	def testAPIRequestBadJSONResponse(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : '{xxxxxxxxx', 'status' : 200})

		self.assertRaisesRegex(SDKBadJSONResponseException, '{xxxxxxxxx', req.exec_)






	def testAPIRequestExpectedStatus(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : '{"X": "X"}', 'status' : 200})
		req.exec_()

		req = APIRequest(PyClient(), '/any/method', 'POST')
		req.call = MagicMock(return_value = {'data' : '{"X": "X"}', 'status' : 200})
		req.exec_()

		req = APIRequest(PyClient(), '/any/method', 'PUT')
		req.call = MagicMock(return_value = {'data' : '{"X": "X"}', 'status' : 200})
		req.exec_()

		req = APIRequest(PyClient(), '/any/method', 'DELETE')
		req.call = MagicMock(return_value = {'data' : '1', 'status' : 204})
		req.exec_()






	def testAPIRequestUnexpectedStatusDELETE(self):
		req = APIRequest(PyClient(), '/any/method', 'DELETE')
		req.call = MagicMock(return_value = {'data' : 'XXXyyy', 'status' : 200})
		self.assertRaisesRegex(SDKErrorResponseException, 'XXXyyy', req.exec_)





	def testAPIRequestUnexpectedStatusGET(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : 'XXXyyy', 'status' : 204})
		self.assertRaisesRegex(SDKErrorResponseException, 'XXXyyy', req.exec_)
	def testAPIRequestUnexpectedStatusPOST(self):
		req = APIRequest(PyClient(), '/any/method', 'POST')
		req.call = MagicMock(return_value = {'data' : 'XXXyyy', 'status' : 204})
		self.assertRaisesRegex(SDKErrorResponseException, 'XXXyyy', req.exec_)
	def testAPIRequestUnexpectedStatusPUT(self):
		req = APIRequest(PyClient(), '/any/method', 'PUT')
		req.call = MagicMock(return_value = {'data' : 'XXXyyy', 'status' : 204})
		self.assertRaisesRegex(SDKErrorResponseException, 'XXXyyy', req.exec_)




	def testAPIRequestEmptyRespGET(self):
		req = APIRequest(PyClient(), '/any/method', 'GET')
		req.call = MagicMock(return_value = {'data' : '{}', 'status' : 200})
		self.assertRaisesRegex(SDKUnexpectedResponseException, 'Empty', req.exec_)
	def testAPIRequestEmptyRespPOST(self):
		req = APIRequest(PyClient(), '/any/method', 'POST')
		req.call = MagicMock(return_value = {'data' : '{}', 'status' : 200})
		self.assertRaisesRegex(SDKUnexpectedResponseException, 'Empty', req.exec_)
	def testAPIRequestEmptyRespPUT(self):
		req = APIRequest(PyClient(), '/any/method', 'PUT')
		req.call = MagicMock(return_value = {'data' : '{}', 'status' : 200})
		self.assertRaisesRegex(SDKUnexpectedResponseException, 'Empty', req.exec_)


if __name__ == '__main__':
	unittest.main()
