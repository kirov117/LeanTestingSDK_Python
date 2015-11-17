from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

from Entity.Platform.PlatformOS import PlatformOS

class PlatformOSHandler(EntityHandler):

    def all(self, filters = None):
        if filters is None:
            filters = {}

        super().all(filters)

        request = APIRequest(self._origin, '/v1/platform/os', 'GET')
        return EntityList(self._origin, request, 'PlatformOS', filters)

    def find(self, id_):
        super().find(id_)

        req = APIRequest(self._origin, '/v1/platform/os/' + id_, 'GET')
        return PlatformOS(self._origin, req.exec_())
