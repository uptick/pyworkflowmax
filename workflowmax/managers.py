import re
import requests

from .endpoints import ENDPOINTS, METHOD_ORDER

WORKFLOWMAX_BASE_URL = "https://api.workflowmax.com"


class Manager():
    def __init__(self, name, credentials):
        self.credentials = credentials
        self.name = name
        self.base_url = '%s/%s.api/' % (WORKFLOWMAX_BASE_URL, name.lower())
        self.method_signatures = {}

        # Build ORM methods from given url endpoints.
        # Sort them first, to determine duplicate disambiguation order.
        import pdb; pdb.set_trace()
        endpoints = sorted(ENDPOINTS[name]['methods'], key=lambda x: METHOD_ORDER.index(x[0]))
        for method, endpoint in endpoints:
            self.build_method(method, endpoint)

    def build_method(self, method, endpoint):
        required_args = re.findall('\[([^\]]*)\]', endpoint)
        template = endpoint.replace('[', '{').replace(']', '}')

        def inner(**kwargs):
            # Build url
            try:
                url = self.base_url + template.format(**kwargs)
            except KeyError as e:
                raise KeyError("Missing arg '%s' while building url. Endpoint requires %s." % (
                    str(e), required_args
                ))

            # Build query
            params = self.credentials.as_params()
            params.update((k, v) for k, v in kwargs.items() if k not in required_args)

            response = requests.request(method, url, params=params)
            # TODO: Handle exceptions coming from response.
            # TODO: Parse XMLResponse before returning
            return response

        # Build method name
        method_name = '_'.join(p for p in endpoint.split('/') if '[' not in p)
        # If it already exists, prepend with method to disambiguate.
        if hasattr(self, method_name):
            method_name = '%s_%s' % (method.lower(), method_name)
        self.method_signatures[method_name] = required_args
        setattr(self, method_name, inner)

    def __repr__(self):
        return '%s%s: [\n    %s\n]' % (self.name, self.__class__.__name__, '\n    '.join(
            '%s(%s)' % (k, ', '.join(v)) for k, v in sorted(self.method_signatures.items())
        ))
