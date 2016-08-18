GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

METHOD_ORDER = [GET, POST, PUT, DELETE]

ENDPOINTS = {
    'Category': {
        'plural': 'categories',
        'methods': [
            (GET, 'list'),
        ],
    },
    'Client': {
        'plural': 'clients',
        'methods': [
            (GET, 'list'),
            (GET, 'search'),
            (GET, 'get/[id]'),
            (POST, 'add'),
            (PUT, 'update'),
            (PUT, 'archive'),
            (POST, 'delete'),
            (GET, 'contact/[id]'),
            (PUT, 'contact/[id]'),
            (POST, 'contact'),
            (DELETE, 'contact/[id]'),
            (GET, 'documents/[id]'),
            (POST, 'document'),
            (POST, 'addrelationship'),
            (POST, 'updaterelationship'),
            (POST, 'deleterelationship'),
        ],
    },
    'ClientGroup': {
        'plural': 'client_groups',
        'methods': [
            (GET, 'list'),
            (GET, 'get/[id]'),
            (POST, 'add'),
            (PUT, 'members'),
            (POST, 'delete'),
        ],
    },
    'Cost': {
        'plural': 'costs',
        'methods': [
            (GET, 'list'),
            (GET, 'get/[id]'),
            (POST, 'add'),
            (PUT, 'update'),
            (POST, 'delete'),
            (POST, 'deleteall'),
        ],
    },
    'CustomField': {
        'plural': 'custom_fields',
        'methods': [
            (GET, 'definition'),
            (GET, 'customfield'),
            (PUT, 'customfield'),
        ],
    },
    'Invoice': {
        'plural': 'invoices',
        'methods': [
            (GET, 'current'),
            (GET, 'get/[invoice number]'),
            (GET, 'draft'),
            (GET, 'job/[job number]'),
            (GET, 'list'),
            (GET, 'payments/[invoice number]'),
        ],
    },
    'Job': {
        'plural': 'jobs',
        'methods': [
            (GET, 'current'),
            (GET, 'get/[job number]'),
            (PUT, 'state'),
            (GET, 'list'),
            (GET, 'staff/[id]'),
            (GET, 'client/[id]'),
            (GET, 'tasks'),
            (POST, 'add'),
            (PUT, 'update'),
            (POST, 'task'),
            (PUT, 'task'),
            (PUT, 'task/[id]/complete'),
            (PUT, 'task/[id]/reopen'),
            (PUT, 'reordertasks'),
            (POST, 'note'),
            (GET, 'documents/[job number]'),
            (POST, 'document'),
            (GET, 'costs/[job number]'),
            (POST, 'cost'),
            (PUT, 'cost'),
            (PUT, 'assign'),
            (POST, 'delete'),
            (POST, 'applytemplate'),
            (POST, 'createquote/[job number]'),
            (POST, 'createestimate/[job number]'),
        ],
    },
    'Lead': {
        'plural': 'leads',
        'methods': [
            (GET, 'current'),
            (GET, 'get/[id]'),
            (GET, 'list'),
            (POST, 'add'),
            (GET, 'categories'),
        ],
    },
    'PurchaseOrder': {
        'plural': 'purchase_orders',
        'methods': [
            (GET, 'current'),
            (GET, 'get/[order number]'),
            (GET, 'draft'),
            (GET, 'list'),
            (GET, 'job/[job number]'),
            (POST, 'add'),
            (POST, 'adddraft'),
        ],
    },
    'Quote': {
        'plural': 'quotes',
        'methods': [
            (GET, 'current'),
            (GET, 'get/[quote number]'),
            (GET, 'draft'),
            (GET, 'list'),
        ],
    },
    'Staff': {
        'plural': 'staff',
        'methods': [
            (GET, 'list'),
            (GET, 'get/[id]'),
            (POST, 'add'),
            (PUT, 'update'),
            (POST, 'delete'),
            (POST, 'enable'),
            (POST, 'disable'),
            (POST, 'forgottenpassword'),
        ],
    },
    'Supplier': {
        'plural': 'suppliers',
        'methods': [
            (GET, 'list'),
            (GET, 'get/[id]'),
            (POST, 'add'),
            (PUT, 'update'),
            (PUT, 'archive'),
            (POST, 'delete'),
            (GET, 'contact/[id]'),
            (PUT, 'contact/[id]'),
            (POST, 'contact'),
        ],
    },
    'Task': {
        'plural': 'tasks',
        'methods': [
            (GET, 'list'),
            (GET, 'get/[id]'),
        ],
    },
    'Template': {
        'plural': 'templates',
        'methods': [
            (GET, 'list'),
        ],
    },
    'Time': {
        'plural': 'times',
        'methods': [
            (GET, 'job/[job number]'),
            (GET, 'list'),
            (GET, 'staff/[id]'),
            (GET, 'get/[id]'),
            (POST, 'add'),
            (PUT, 'update'),
            (DELETE, 'delete/[id]'),
        ],
    },
}
