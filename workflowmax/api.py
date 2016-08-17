from .endpoints import ENDPOINTS
from .managers import Manager


class WorkflowMax:
    """An ORM-like interface to the WorkflowMax API"""

    def __init__(self, credentials):
        self.credentials = credentials

        for k, v in ENDPOINTS.items():
            setattr(self, v['plural'], Manager(k, credentials))
