WORKFLOWMAX_BASE_URL = "https://api.workflowmax.com"

import requests

from .endpoints import ENDPOINTS


class Manager():
    def __init__(self, name, credentials):
        self.credentials = credentials
        self.name = name
        self.base_url = '%s/%s.api/' % (WORKFLOWMAX_BASE_URL, name.lower())

        # Build ORM methods from given url endpoints
        for method, endpoint in ENDPOINTS[name]['methods']:
            # TODO: Parse [] bits out of endpoint and use to construct expected param.
            try:
                getattr(self, '_%s' % endpoint)()
            except AttributeError:
                # TODO: Warn about unprepared endpoint.
                pass

    def _list(self):
        """ The "list" endpoint enables use of `all` and `filter`."""

        def inner(**kwargs):
            params = self.credentials.as_params()
            params.update(kwargs)

            response = requests.get(
                self.base_url + 'list',
                params=params
            )
            # TODO: Handle exceptions
            # TODO: Parse XMLResponse before returning
            return response

        setattr(self, 'all', inner)
        setattr(self, 'filter', inner)

    def __repr__(self):
        return '%sManager()' % (self.name, )
