import sys
import os

import unittest2 as unittest
from unittest.mock import MagicMock

# adds current SDK path to sys.path for imports
sys.path.insert(0, os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../../LeanTestingSDK'))

from PyClient import PyClient

from Exception.SDKIncompleteRequestException	import SDKIncompleteRequestException
from Exception.SDKUnsupportedRequestException	import SDKUnsupportedRequestException
from Exception.SDKInvalidArgException			import SDKInvalidArgException
from Exception.SDKErrorResponseException		import SDKErrorResponseException

class LiveRequestsTest(unittest.TestCase):

	_client = None

	_sampleProjectID = 3515
	_sampleBugID = 38483
	_sampleOrganizationID = 2464
	_sampleAttachmmentID = 21515
	_samplePlatformTypeID = 1
	_sampleDeviceID = 11
	_sampleOSID = 1
	_sampleBrowserId = 1


	def setUp(self):
		self._client = PyClient()
		self._client.attachToken('6cOb1uNIMFyyJQdK33N9lxjECw5AJom1L3iKcVPw')



	# USER
	def testGetUserInformation(self):
		info = self._client.user.getInformation()

		self.assertIsInstance(info, dict)

		self.assertTrue('id' in info)
		self.assertTrue('username' in info)
		self.assertTrue('first_name' in info)
		self.assertTrue('last_name' in info)
		self.assertTrue('email' in info)
	def testGetUserOrganizations(self):
		org = self._client.user.organizations.all().toArray()

		self.assertIsInstance(org, list)

		self.assertTrue(len(org) >= 1)

		self.assertTrue('id' in org[0])
		self.assertTrue('name' in org[0])
	# END USER




	# PROJECT
	def testListAllProjects(self):
		prj = self._client.projects.all().toArray()

		self.assertIsInstance(prj, list)

		self.assertTrue(len(prj) >= 1)

		self.assertTrue('id' in prj[0])
		self.assertTrue('name' in prj[0])
		self.assertTrue('owner_id' in prj[0])
		self.assertTrue('organization_id' in prj[0])
	def testCreateNewProject(self):
		_name = 'Project135'
		_orgid = self._sampleOrganizationID

		newProject = self._client.projects.create({
			'name': _name,
			'organization_id': _orgid
		})

		data = newProject.data

		self.assertIsInstance(data, dict)

		self.assertTrue('id' in data)
		self.assertTrue('name' in data)
		self.assertTrue('owner_id' in data)
		self.assertTrue('organization_id' in data)

		self.assertEqual(_name, data['name'])
		self.assertEqual(_orgid, data['organization_id'])
	def testRetrieveExistingProject(self):
		project = self._client.projects.find(self._sampleProjectID).data

		self.assertIsInstance(project, dict)

		self.assertTrue('id' in project)
		self.assertTrue('name' in project)
		self.assertTrue('owner_id' in project)
		self.assertTrue('organization_id' in project)

	def testListProjectSections(self):
		sect = self._client.projects.find(self._sampleProjectID).sections.all().toArray()

		self.assertIsInstance(sect, list)

		self.assertTrue(len(sect) >= 1)

		self.assertTrue('id' in sect[0])
		self.assertTrue('name' in sect[0])
		self.assertTrue('project_id' in sect[0])
	def testAddProjectSection(self):
		_name = 'SectionName999'

		newSection = self._client.projects.find(self._sampleProjectID).sections.create({
			'name': _name
		})

		data = newSection.data

		self.assertIsInstance(data, dict)

		self.assertTrue('id' in data)
		self.assertTrue('name' in data)
		self.assertTrue('project_id' in data)

		self.assertEqual(_name, data['name'])

	def testListProjectVersions(self):
		vers = self._client.projects.find(self._sampleProjectID).versions.all().toArray()

		self.assertIsInstance(vers, list)

		self.assertTrue(len(vers) >= 1)

		self.assertTrue('id' in vers[0])
		self.assertTrue('number' in vers[0])
		self.assertTrue('project_id' in vers[0])
	def testAddProjectVersion(self):
		_number = 'v2.0.0'

		newVersion = self._client.projects.find(self._sampleProjectID).versions.create({
			'number': _number
		})

		data = newVersion.data

		self.assertIsInstance(data, dict)

		self.assertTrue('id' in data)
		self.assertTrue('number' in data)
		self.assertTrue('project_id' in data)

		self.assertEqual(_number, data['number'])

	def testListProjectUsers(self):
		usr = self._client.projects.find(self._sampleProjectID).users.all().toArray()

		self.assertIsInstance(usr, list)

		self.assertTrue(len(usr) >= 1)

		self.assertTrue('id' in usr[0])
		self.assertTrue('username' in usr[0])
		self.assertTrue('first_name' in usr[0])
		self.assertTrue('last_name' in usr[0])
		self.assertTrue('email' in usr[0])

	def testListProjectBugTypeScheme(self):
		scheme = self._client.projects.find(self._sampleProjectID).bugTypeScheme.all().toArray()

		self.assertIsInstance(scheme, list)

		self.assertTrue(len(scheme) >= 1)

		self.assertTrue('id' in scheme[0])
		self.assertTrue('name' in scheme[0])
	def testListProjectBugStatusScheme(self):
		scheme = self._client.projects.find(self._sampleProjectID).bugStatusScheme.all().toArray()

		self.assertIsInstance(scheme, list)

		self.assertTrue(len(scheme) >= 1)

		self.assertTrue('id' in scheme[0])
		self.assertTrue('name' in scheme[0])
	def testListProjectBugSeverityScheme(self):
		scheme = self._client.projects.find(self._sampleProjectID).bugSeverityScheme.all().toArray()

		self.assertIsInstance(scheme, list)

		self.assertTrue(len(scheme) >= 1)

		self.assertTrue('id' in scheme[0])
		self.assertTrue('name' in scheme[0])
	def testListProjectBugReproducibilityScheme(self):
		scheme = self._client.projects.find(self._sampleProjectID).bugReproducibilityScheme.all().toArray()

		self.assertIsInstance(scheme, list)

		self.assertTrue(len(scheme) >= 1)

		self.assertTrue('id' in scheme[0])
		self.assertTrue('name' in scheme[0])
	# END PROJECT



	# BUG
	def testListBugsInProject(self):
		bugs = self._client.projects.find(self._sampleProjectID).bugs.all().toArray()

		self.assertIsInstance(bugs, list)

		self.assertTrue(len(bugs) >= 1)

		self.assertTrue('id' in bugs[0])
		self.assertTrue('title' in bugs[0])
		self.assertTrue('status_id' in bugs[0])
		self.assertTrue('severity_id' in bugs[0])
		self.assertTrue('project_version_id' in bugs[0])
		self.assertTrue('project_section_id' in bugs[0])
		self.assertTrue('type_id' in bugs[0])
		self.assertTrue('reproducibility_id' in bugs[0])
		self.assertTrue('assigned_user_id' in bugs[0])
		self.assertTrue('description' in bugs[0])
		self.assertTrue('expected_results' in bugs[0])
	def testCreateNewBug(self):
		_title = 'Bugzilla000111'
		_status_id = 2
		_severity_id = 2
		_project_version_id = 10242
		_project_section_id = 12675
		_type_id = 4
		_reproducibility_id = 2
		_assigned_user_id = 4650
		_description = 'Descrdescrdescr'
		_expected_results = 'Expecexpecexpec'
		_steps = ['first do this', 'then do that', 'finally...']
		_platform = {'device_model_id': 11, 'os': 'Android', 'os_version_id': 207}


		newBug = self._client.projects.find(self._sampleProjectID).bugs.create({
			'title': _title,
			'status_id': _status_id,
			'severity_id': _severity_id,
			'project_version_id': _project_version_id,
			'project_section_id': _project_section_id,
			'type_id': _type_id,
			'reproducibility_id': _reproducibility_id,
			'assigned_user_id': _assigned_user_id,
			'description': _description,
			'expected_results': _expected_results,
			'steps': _steps,
			'platform': _platform
		})

		data = newBug.data

		self.assertIsInstance(data, dict)

		self.assertTrue('id' in data)
		self.assertTrue('title' in data)
		self.assertTrue('status_id' in data)
		self.assertTrue('severity_id' in data)
		self.assertTrue('project_version_id' in data)
		self.assertTrue('project_section_id' in data)
		self.assertTrue('type_id' in data)
		self.assertTrue('reproducibility_id' in data)
		self.assertTrue('assigned_user_id' in data)
		self.assertTrue('description' in data)
		self.assertTrue('expected_results' in data)
		self.assertTrue('steps' in data)
		self.assertTrue('platform' in data)

		self.assertIsInstance(data['steps'], list)
		self.assertIsInstance(data['platform'], dict)

		self.assertEqual(3, len(data['steps']))

		self.assertEqual(_title, data['title'])
		self.assertEqual(_status_id, data['status_id'])
		self.assertEqual(_severity_id, data['severity_id'])
		self.assertEqual(_project_version_id, data['project_version_id'])
		self.assertEqual(_project_section_id, data['project_section_id'])
		self.assertEqual(_type_id, data['type_id'])
		self.assertEqual(_reproducibility_id, data['reproducibility_id'])
		self.assertEqual(_assigned_user_id, data['assigned_user_id'])
		self.assertEqual(_description, data['description'])
		self.assertEqual(_expected_results, data['expected_results'])

		self.assertEqual(_steps[0], data['steps'][0]['text'])

		self.assertEqual(_platform['device_model_id'], data['platform']['model']['id'])
		self.assertEqual(_platform['os'], data['platform']['os']['name'])
		self.assertEqual(_platform['os_version_id'], data['platform']['os_version']['id'])
	def testRetrieveExistingBug(self):
		bug = self._client.bugs.find(self._sampleBugID).data

		self.assertIsInstance(bug, dict)

		self.assertTrue('id' in bug)
		self.assertTrue('title' in bug)
		self.assertTrue('status_id' in bug)
		self.assertTrue('severity_id' in bug)
		self.assertTrue('project_version_id' in bug)
		self.assertTrue('project_section_id' in bug)
		self.assertTrue('type_id' in bug)
		self.assertTrue('reproducibility_id' in bug)
		self.assertTrue('assigned_user_id' in bug)
		self.assertTrue('description' in bug)
		self.assertTrue('expected_results' in bug)
	def testUpdateBug(self):
		_title = 'Upddssszz'
		_status_id = 1
		_severity_id = 1
		_project_version_id = 10242
		_project_section_id = 12675
		_type_id = 3
		_assigned_user_id = 4650
		_description = 'NJSDESCR'
		_expected_results = 'NJSXEXPR'


		updatedBug = self._client.bugs.update(self._sampleBugID, {
			'title': _title,
			'status_id': _status_id,
			'severity_id': _severity_id,
			'project_version_id': _project_version_id,
			'project_section_id': _project_section_id,
			'type_id': _type_id,
			'assigned_user_id': _assigned_user_id,
			'description': _description,
			'expected_results': _expected_results
		})

		data = updatedBug.data

		self.assertIsInstance(data, dict)

		self.assertTrue('id' in data)
		self.assertTrue('title' in data)
		self.assertTrue('status_id' in data)
		self.assertTrue('severity_id' in data)
		self.assertTrue('project_version_id' in data)
		self.assertTrue('project_section_id' in data)
		self.assertTrue('type_id' in data)
		self.assertTrue('assigned_user_id' in data)
		self.assertTrue('description' in data)
		self.assertTrue('expected_results' in data)

		self.assertEqual(_title, data['title'])
		self.assertEqual(_status_id, data['status_id'])
		self.assertEqual(_severity_id, data['severity_id'])
		self.assertEqual(_project_version_id, data['project_version_id'])
		self.assertEqual(_project_section_id, data['project_section_id'])
		self.assertEqual(_type_id, data['type_id'])
		self.assertEqual(_assigned_user_id, data['assigned_user_id'])
		self.assertEqual(_description, data['description'])
		self.assertEqual(_expected_results, data['expected_results'])
	# END BUG



	# BUG COMMENTS
	def testListBugComments(self):
		comments = self._client.bugs.find(self._sampleBugID).comments.all().toArray()

		self.assertIsInstance(comments, list)

		self.assertTrue(len(comments) >= 1)

		self.assertTrue('id' in comments[0])
		self.assertTrue('text' in comments[0])
		self.assertTrue('owner_id' in comments[0])
	# END BUG COMMENTS




	# BUG ATTACHMENTS
	def testListBugAttachments(self):
		atc = self._client.bugs.find(self._sampleBugID).attachments.all().toArray()

		self.assertIsInstance(atc, list)

		self.assertTrue(len(atc) >= 1)

		self.assertTrue('id' in atc[0])
		self.assertTrue('owner_id' in atc[0])
		self.assertTrue('url' in atc[0])
	def testCreateNewAttachment(self):
		_fp = os.path.dirname(os.path.realpath(__file__)) + '/../res/upload_sample.jpg'

		new_attachment = self._client.bugs.find(self._sampleBugID).attachments.upload(_fp)

		data = new_attachment.data

		self.assertIsInstance(data, dict)

		self.assertTrue('id' in data)
		self.assertTrue('owner_id' in data)
		self.assertTrue('url' in data)
	def testRetrieveExistingAttachment(self):
		atc = self._client.attachments.find(self._sampleAttachmmentID).data

		self.assertIsInstance(atc, dict)

		self.assertTrue('id' in atc)
		self.assertTrue('owner_id' in atc)
		self.assertTrue('url' in atc)
	# END BUG ATTACHMENTS





	# PLATFORM
	def testListPlatformTypes(self):
		types = self._client.platform.types.all().toArray()

		self.assertIsInstance(types, list)

		self.assertTrue(len(types) >= 1)

		self.assertTrue('id' in types[0])
		self.assertTrue('name' in types[0])
	def testRetrievePlatformType(self):
		type_ = self._client.platform.types.find(self._samplePlatformTypeID).data

		self.assertIsInstance(type_, dict)

		self.assertTrue('id' in type_)
		self.assertTrue('name' in type_)

	def testListPlatformDevices(self):
		devs = self._client.platform.types.find(self._samplePlatformTypeID).devices.all().toArray()

		self.assertIsInstance(devs, list)

		self.assertTrue(len(devs) >= 1)

		self.assertTrue('id' in devs[0])
		self.assertTrue('name' in devs[0])
	def testRetrievePlatformDevice(self):
		dev = self._client.platform.devices.find(self._sampleDeviceID).data

		self.assertIsInstance(dev, dict)

		self.assertTrue('id' in dev)
		self.assertTrue('name' in dev)

	def testListOS(self):
		os = self._client.platform.os.all().toArray()

		self.assertIsInstance(os, list)

		self.assertTrue(len(os) >= 1)

		self.assertTrue('id' in os[0])
		self.assertTrue('name' in os[0])
	def testRetrieveOS(self):
		os = self._client.platform.os.find(self._sampleOSID).data

		self.assertIsInstance(os, dict)

		self.assertTrue('id' in os)
		self.assertTrue('name' in os)
	def testListOSVersions(self):
		osv = self._client.platform.os.find(self._sampleOSID).versions.all().toArray()

		self.assertIsInstance(osv, list)

		self.assertTrue(len(osv) >= 1)

		self.assertTrue('id' in osv[0])
		self.assertTrue('number' in osv[0])

	def testListBrowsers(self):
		browsers = self._client.platform.browsers.all().toArray()

		self.assertIsInstance(browsers, list)

		self.assertTrue(len(browsers) >= 1)

		self.assertTrue('id' in browsers[0])
		self.assertTrue('name' in browsers[0])
	def testRetrieveBrowser(self):
		browser = self._client.platform.browsers.find(self._sampleBrowserId).data

		self.assertIsInstance(browser, dict)

		self.assertTrue('id' in browser)
		self.assertTrue('name' in browser)
	def testListBrowserVersions(self):
		brw = self._client.platform.browsers.find(self._sampleBrowserId).versions.all().toArray()

		self.assertIsInstance(brw, list)

		self.assertTrue(len(brw) >= 1)

		self.assertTrue('id' in brw[0])
		self.assertTrue('name' in brw[0])
	# END PLATFORM



	# INVALID FIELDS
	def testCreateNewProjectIncomplete(self):
		self.assertRaisesRegex(SDKIncompleteRequestException, 'name', self._client.projects.create, {'organization_id': 0})
	def testCreateNewProjectUnsupported(self):
		self.assertRaisesRegex(SDKUnsupportedRequestException, 'fxxxxxx', self._client.projects.create, {'name': '', 'fxxxxxx': ''})

	def testAddProjectSectionUnsupported(self):
		p = self._client.projects.find(self._sampleProjectID)
		self.assertRaisesRegex(SDKUnsupportedRequestException, 'fxxxxxx', p.sections.create, {'name': '', 'fxxxxxx': ''})

	def testAddProjectVersionUnsupported(self):
		p = self._client.projects.find(self._sampleProjectID)
		self.assertRaisesRegex(SDKUnsupportedRequestException, 'fxxxxxx', p.versions.create, {'number': '', 'fxxxxxx': ''})

	def testCreateNewBugIncomplete(self):
		_title = 'Bugzilla000111'
		_status_id = 2
		_severity_id = 2

		p = self._client.projects.find(self._sampleProjectID)
		self.assertRaisesRegex(SDKIncompleteRequestException, 'project_version', p.bugs.create,
			{'title': _title, 'status_id': _status_id, 'severity_id': _severity_id})

	def testCreateNewBugUnsupported(self):
		_title = 'Bugzilla000111'
		_status_id = 2
		_severity_id = 2
		_project_version_id = 10242

		p = self._client.projects.find(self._sampleProjectID)

		self.assertRaisesRegex(SDKUnsupportedRequestException, 'fxxxxxx', p.bugs.create,
			{'title': _title, 'status_id': _status_id, 'severity_id': _severity_id, 'project_version_id': _project_version_id, 'fxxxxxx': ''})

	def testCreateNewAttachmentNonStrFilepath(self):
		b = self._client.bugs.find(self._sampleBugID)
		self.assertRaisesRegex(SDKInvalidArgException, 'filepath', b.attachments.upload, 111)
	# END INVALID FIELDS




	# MISC
	def testForbiddenResponse(self):
		self.assertRaisesRegex(SDKErrorResponseException, 'forbidden', self._client.bugs.find, 1)
	def testMissingResponse(self):
		self.assertRaisesRegex(SDKErrorResponseException, '404', self._client.bugs.find, 999999)
	def testInvalidToken(self):
		self._client.attachToken('6cOb1uNIMFyyJQdK33N9lxjECw5AJom1L3xxxxxx')
		self.assertRaisesRegex(SDKErrorResponseException, 'denied', self._client.projects.find, self._sampleProjectID)
	def testNoToken(self):
		cl = PyClient()
		self.assertRaisesRegex(SDKErrorResponseException, 'access token', cl.projects.find, self._sampleProjectID)
	# END MISC


if __name__ == '__main__':
	unittest.main()
