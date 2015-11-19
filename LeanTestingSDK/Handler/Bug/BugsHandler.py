from BaseClass.EntityHandler    import EntityHandler
from BaseClass.APIRequest       import APIRequest

from Entity.Bug.Bug import Bug

class BugsHandler(EntityHandler):

	def find(self, id_):
		super().find(id_)

		req = APIRequest(self._origin, '/v1/bugs/' + str(id_), 'GET')
		return Bug(self._origin, req.exec_())

	def delete(self, id_):
		super().delete(id_)

		req = APIRequest(self._origin, '/v1/bugs/' + str(id_), 'DELETE')
		return req.exec_()

	def update(self, id_, fields):
		super().update(id_, fields)

		supports = {
			'title'              : False,
			'status_id'          : False,
			'severity_id'        : False,
			'project_version_id' : False,
			'project_section_id' : False,
			'type_id'            : False,
			'assigned_user_id'   : False,
			'description'        : False,
			'expected_results'   : False,
			'steps'              : False,
			'platform'           : False
			# 'device_model'       : False,
			# 'device_model_id'    : False,
			# 'os'                 : False,
			# 'os_version'         : False,
			# 'os_version_id'      : False,
			# 'browser_version_id' : False
		}

		if self.enforce(fields, supports):
			req = APIRequest(self._origin, '/v1/bugs/' + str(id_), 'PUT', {'params': fields})
			return Bug(self._origin, req.exec_())
