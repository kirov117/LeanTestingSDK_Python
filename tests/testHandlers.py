import sys
import os

import unittest2 as unittest

# adds current SDK path to sys.path for imports
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../LeanTestingSDK'))

from PyClient import PyClient

from Exception.SDKInvalidArgException import SDKInvalidArgException

from Handler.Attachment.AttachmentsHandler	import AttachmentsHandler

from Handler.Bug.BugsHandler			import BugsHandler
from Handler.Bug.BugCommentsHandler		import BugCommentsHandler
from Handler.Bug.BugAttachmentsHandler	import BugAttachmentsHandler

from Handler.Platform.PlatformHandler					import PlatformHandler
from Handler.Platform.PlatformTypesHandler				import PlatformTypesHandler
from Handler.Platform.PlatformBrowsersHandler			import PlatformBrowsersHandler
from Handler.Platform.PlatformBrowserVersionsHandler	import PlatformBrowserVersionsHandler
from Handler.Platform.PlatformOSHandler					import PlatformOSHandler
from Handler.Platform.PlatformOSVersionsHandler			import PlatformOSVersionsHandler
from Handler.Platform.PlatformTypeDevicesHandler		import PlatformTypeDevicesHandler
from Handler.Platform.PlatformDevicesHandler			import PlatformDevicesHandler

from Handler.Project.ProjectsHandler	import ProjectsHandler

from Handler.Project.ProjectSectionsHandler	import ProjectSectionsHandler
from Handler.Project.ProjectVersionsHandler	import ProjectVersionsHandler
from Handler.Project.ProjectUsersHandler	import ProjectUsersHandler

from Handler.Project.ProjectBugTypeSchemeHandler			import ProjectBugTypeSchemeHandler
from Handler.Project.ProjectBugStatusSchemeHandler			import ProjectBugStatusSchemeHandler
from Handler.Project.ProjectBugSeveritySchemeHandler		import ProjectBugSeveritySchemeHandler
from Handler.Project.ProjectBugReproducibilitySchemeHandler	import ProjectBugReproducibilitySchemeHandler

from Handler.Project.ProjectBugsHandler	import ProjectBugsHandler

from Handler.User.UserHandler				import UserHandler
from Handler.User.UserOrganizationsHandler	import UserOrganizationsHandler

class HandlersTest(unittest.TestCase):

	_handlerCollection = [
		[AttachmentsHandler],
		[BugAttachmentsHandler,						'requiresIDInConstructor'],
		[BugCommentsHandler,						'requiresIDInConstructor'],
		[BugsHandler],
		[PlatformBrowsersHandler],
		[PlatformBrowserVersionsHandler,			'requiresIDInConstructor'],
		[PlatformDevicesHandler],
		[PlatformHandler],
		[PlatformOSHandler],
		[PlatformOSVersionsHandler,					'requiresIDInConstructor'],
		[PlatformTypeDevicesHandler,				'requiresIDInConstructor'],
		[PlatformTypesHandler],
		[ProjectBugReproducibilitySchemeHandler,	'requiresIDInConstructor'],
		[ProjectBugSeveritySchemeHandler,			'requiresIDInConstructor'],
		[ProjectBugsHandler,						'requiresIDInConstructor'],
		[ProjectBugStatusSchemeHandler,				'requiresIDInConstructor'],
		[ProjectBugTypeSchemeHandler,				'requiresIDInConstructor'],
		[ProjectSectionsHandler,					'requiresIDInConstructor'],
		[ProjectsHandler],
		[ProjectUsersHandler,						'requiresIDInConstructor'],
		[ProjectVersionsHandler,					'requiresIDInConstructor'],
		[UserHandler],
		[UserOrganizationsHandler]
	]


	def testHandlersDefined(self):
		for e in self._handlerCollection:
			e[0]




	def testHandlersCreateNonArrFields(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.create, '')
	def testHandlersCreateEmptyFields(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.create, {})





	def testHandlersAllNonArrFilters(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.all, '')
	def testHandlersAllInvalidFilters(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.all, {'XXXfilterXXX': 9999})
	def testHandlersAllSupportedFilters(self):
		client = PyClient()
		client.debugReturn = {
			'data': '{"x": [], "meta": {"pagination": {}}}',
			'status': 200
		}

		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](client, 999)
			else:
				inst = e[0](client)

			inst.all({'include': ''})
			inst.all({'limit': 10})
			inst.all({'page': 2})





	def testHandlersFindNonIntID(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.find, '')




	def testHandlersDeleteNonIntID(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.delete, '')





	def testHandlersUpdateNonIntID(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.update, '', {'x': 5})
	def testHandlersUpdateNonArrFields(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.update, 5, '')
	def testHandlersUpdateEmptyFields(self):
		for e in self._handlerCollection:
			if 0 <= 1 < len(e) and e[1] == 'requiresIDInConstructor':
				inst = e[0](PyClient(), 999)
			else:
				inst = e[0](PyClient())
			self.assertRaises(SDKInvalidArgException, inst.update, 5, {})





	# HAVE SECONDARIES
	def testPlatformHandlerHasTypes(self):
		self.assertIsInstance(PlatformHandler(PyClient()).types, PlatformTypesHandler)
	def testPlatformHandlerHasDevices(self):
		self.assertIsInstance(PlatformHandler(PyClient()).devices, PlatformDevicesHandler)
	def testPlatformHandlerHasOS(self):
		self.assertIsInstance(PlatformHandler(PyClient()).os, PlatformOSHandler)
	def testPlatformHandlerHasBrowsers(self):
		self.assertIsInstance(PlatformHandler(PyClient()).browsers, PlatformBrowsersHandler)
	def testUserHandlerHasOrganizations(self):
		self.assertIsInstance(UserHandler(PyClient()).organizations, UserOrganizationsHandler)
	# END HAVE SECONDARIES



if __name__ == '__main__':
	unittest.main()
