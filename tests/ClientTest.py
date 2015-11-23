import sys
import os

import unittest2 as unittest

# adds current SDK path to sys.path for imports
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../LeanTestingSDK'))

from PyClient import PyClient

from Exception.SDKInvalidArgException import SDKInvalidArgException

from Handler.Auth.OAuth2Handler				import OAuth2Handler
from Handler.User.UserHandler				import UserHandler
from Handler.Project.ProjectsHandler		import ProjectsHandler
from Handler.Bug.BugsHandler				import BugsHandler
from Handler.Attachment.AttachmentsHandler	import AttachmentsHandler
from Handler.Platform.PlatformHandler		import PlatformHandler

class ClientTest(unittest.TestCase):

	def testClientDefined(self):
		PyClient



	def testClientHasAuthObj(self):
		self.assertIsInstance(PyClient().auth, OAuth2Handler)
	def testClientHasUserObj(self):
		self.assertIsInstance(PyClient().user, UserHandler)
	def testClientHasProjectsObj(self):
		self.assertIsInstance(PyClient().projects, ProjectsHandler)
	def testClientHasBugsObj(self):
		self.assertIsInstance(PyClient().bugs, BugsHandler)
	def testClientHasAttachmentsObj(self):
		self.assertIsInstance(PyClient().attachments, AttachmentsHandler)
	def testClientHasPlatformObj(self):
		self.assertIsInstance(PyClient().platform, PlatformHandler)



	def testInitialEmptyToken(self):
		self.assertFalse(PyClient().getCurrentToken())
	def testTokenParseStorage(self):
		tokenName = '__token__test__'
		client = PyClient()
		client.attachToken(tokenName)
		self.assertEqual(client.getCurrentToken(), tokenName)
	def testTokenParseNonStr(self):
		self.assertRaises(SDKInvalidArgException, PyClient().attachToken, 7182381)



if __name__ == '__main__':
	unittest.main()
