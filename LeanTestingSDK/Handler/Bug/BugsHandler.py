from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

from Entity.Bug.Bug import Bug

class BugsHandler(EntityHandler):

    def find(self, id_):
        super().find(id_)

        req = APIRequest(self._origin, '/v1/bugs/' + id_, 'GET')
        return Bug(self._origin, req.exec_())

    def delete(self, id_):
        super().delete(id_)

        req = APIRequest(self._origin, '/v1/bugs/' + id_, 'DELETE')
        return req.exec_()

    def update(self, id_, fields):
        super().update(id_, fields)

        supports = {
            'title'              : OPTIONAL,
            'status_id'          : OPTIONAL,
            'severity_id'        : OPTIONAL,
            'project_version_id' : OPTIONAL,
            'project_section_id' : OPTIONAL,
            'type_id'            : OPTIONAL,
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
            req = APIRequest(self._origin, '/v1/bugs/' + id_, 'PUT', {'params': fields})
            return Bug(self._origin, req.exec_())
