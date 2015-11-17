from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

class PlatformBrowserVersionsHandler(EntityHandler):

	_browserID = None

	def __init__(self, origin, browserID):
		super().__init__(origin)

		self._browserID = browserID

	def all(self, filters = None):
		if filters is None:
			filters = {}

		super().all(filters)

		request = APIRequest(self._origin, '/v1/platform/browsers/' + self._browserID + '/versions', 'GET')
		return EntityList(self._origin, request, 'PlatformBrowserVersion', filters)
