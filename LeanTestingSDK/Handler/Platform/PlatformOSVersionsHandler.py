from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

class PlatformOSVersionsHandler(EntityHandler):

	_osID = None

	def __init__(self, origin, osID):
		super().__init__(origin)

		self._osID = osID

	def all(self, filters = None):
		if filters is None:
			filters = {}

		super().all(filters)

		request = APIRequest(self._origin, '/v1/platform/os/' + self._osID + '/versions', 'GET')
		return EntityList(self._origin, request, 'PlatformOSVersion', filters)
