from .credentials import Credentials
from .endpoints import ENDPOINTS
from .managers import Manager


class WorkflowMax:
    """An ORM-like interface to the WorkflowMax API"""

    def __init__(self, credentials):
        if not isinstance(credentials, Credentials):
            raise TypeError(
                'Expected a Credentials instance, got %s.' % (
                    type(credentials).__name__,
                )
            )
        self.credentials = credentials

        for k, v in ENDPOINTS.items():
            setattr(self, v['plural'], Manager(k, credentials))

    def __repr__(self):
        return '%s:\n    %s' % (self.__class__.__name__, '\n    '.join(
            sorted(v['plural'] for v in ENDPOINTS.values())
        ))
