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
            'title'              : REQUIRED,
            'status_id'          : REQUIRED,
            'severity_id'        : REQUIRED,
            'project_version'    : REQUIRED,
            'project_version_id' : REQUIRED,
            'project_section_id' : OPTIONAL,
            'type_id'            : OPTIONAL,
            'reproducibility_id' : OPTIONAL,
            'assigned_user_id'   : OPTIONAL,
            'description'        : OPTIONAL,
            'expected_results'   : OPTIONAL,
            'steps'              : OPTIONAL,
            'platform'           : OPTIONAL,
            'device_model'       : OPTIONAL,
            'device_model_id'    : OPTIONAL,
            'os'                 : OPTIONAL,
            'os_version'         : OPTIONAL,
            'os_version_id'      : OPTIONAL,
            'browser_version_id' : OPTIONAL
        }

        if self.enforce(fields, supports):
            req = APIRequest(
                self._origin,
                '/v1/projects/' + self._projectID + '/bugs',
                'POST',
                {'params': fields}
            )

            return Bug(self._origin, req.exec_())

    def all(self, filters = None):
        if filters is None:
            filters = {}

        super().all(filters)

        request = APIRequest(self._origin, '/v1/projects/' + self._projectID + '/bugs', 'GET')
        return EntityList(self._origin, request, 'Bug', filters)
