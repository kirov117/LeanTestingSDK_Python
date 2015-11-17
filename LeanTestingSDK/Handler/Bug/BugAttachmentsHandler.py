from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

class BugAttachmentsHandler(EntityHandler):

    _bugID = None

    def __init__(self, origin, bugID):
        super().__init__(origin)

        self._bugID = bugID

    def upload(self, filepath):
        #TODO
        pass

    def all(self, filters = None):
        if filters is None:
            filters = {}

        request = APIRequest(self._origin, '/v1/bugs/' + self._bugID + '/attachments', 'GET')
        return EntityList(self._origin, request, 'BugAttachment', filters)
