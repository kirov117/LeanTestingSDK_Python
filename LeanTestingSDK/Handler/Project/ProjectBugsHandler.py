from BaseClass.EntityList       import EntityList
from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

from Entity.Bug.Bug import Bug

class ProjectBugsHandler(EntityHandler):

    _projectID = None

    def __init__(self, origin, projectID):
        super().__init__(origin)

        self._projectID = projectID

    def create(self, fields):
        super().create(fields)

        supports = {
            'title'              : True,
            'status_id'          : True,
            'severity_id'        : True,
            'project_version'    : True,
            'project_version_id' : True,
            'project_section_id' : False,
            'type_id'            : False,
            'reproducibility_id' : False,
            'assigned_user_id'   : False,
            'description'        : False,
            'expected_results'   : False,
            'steps'              : False,
            'platform'           : False
            # 'device_model'       : OPTIONAL,
            # 'device_model_id'    : OPTIONAL,
            # 'os'                 : OPTIONAL,
            # 'os_version'         : OPTIONAL,
            # 'os_version_id'      : OPTIONAL,
            # 'browser_version_id' : OPTIONAL
        }

        if 'project_version_id' in fields.keys():
            supports['project_version'] = OPTIONAL
        elif 'project_version' in fields.keys():
            supports['project_version_id'] = OPTIONAL

        if self.enforce(fields, supports):
            req = APIRequest(
                self._origin,
                '/v1/projects/' + str(self._projectID) + '/bugs',
                'POST',
                {'params': fields}
            )

            return Bug(self._origin, req.exec_())

    def all(self, filters = None):
        if filters is None:
            filters = {}

        super().all(filters)

        request = APIRequest(self._origin, '/v1/projects/' + str(self._projectID) + '/bugs', 'GET')
        return EntityList(self._origin, request, Bug, filters)
