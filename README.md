# PyWorkflowMax

PyWorkflowMax is a Python API for accessing the REST API provided by the [WorkflowMax](https://www.workflowmax.com/api/)
job management tool.

## Getting started

Install:
```
pip install pyworkflowmax
```

Create a `Credentials` instance and provide your API and account keys:
```
from workflowmax import Credentials

cred = Credentials(
  api_key=os.environ.get('WORKFLOWMAX_API_KEY'),
  account_key=os.environ.get('WORKFLOWMAX_ACCOUNT_KEY')
)
```

Create a `WorkflowMax` instance, supplying the credentials:
```
from workflowmax import WorkflowMax

wfm = WorkflowMax(cred)
```

Access stuff:
```
important_clients = wfm.clients.search(query='VIP')
```

If you don't know what you're looking for:

- the repr of a `WorkFlowMax` instance will yield a list of available managers (i.e. `clients` in the above example).
- the repr of a `Manager` instance will yield a list of available methods on that manager. Each method corresponds to an API call in WorkFlowMax.


## Development

This project is still a baby. It has no tests, limited post/patch functionality, and supports Python 3 only.

Contributions are welcome. ;)
