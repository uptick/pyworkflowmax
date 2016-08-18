from .endpoints import ENDPOINTS
from .managers import Manager


class WorkflowMax:
    """An ORM-like interface to the WorkflowMax API"""

    def __init__(self, credentials):
        self.credentials = credentials

        for k, v in ENDPOINTS.items():
            setattr(self, v['plural'], Manager(k, credentials))

    def __repr__(self):
        return '%s:\n    %s' % (self.__class__.__name__, '\n    '.join(
            v['plural'] for v in ENDPOINTS.values()
        ))
