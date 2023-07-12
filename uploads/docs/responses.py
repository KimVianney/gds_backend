from drf_yasg import openapi


CREATE_UPLOAD_RESPONSE = {
    '201': openapi.Response(
        description='User has successfully added eye image uploads',
        examples={
            'application/json': {
                'message': 'Done',
                'upload': {
                    'id': 0,
                    'uuid': 'string',
                    'description': 'string',
                    'images': ['url']
                }
            }
        }
    ),
    '400': openapi.Response(
        description='User sent an invalid request body',
        examples={
            'application/json': {
                'message': 'Invalid values',
                'error': {}
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
}

FETCH_UPLOADS_RESPONSE = {
    '200': openapi.Response(
        description='User has successfully retrieved their eye image uploads',
        examples={
            'application/json': {
                'message': 'Done',
                'uploads': [],
                'previous': 'string',
                'next': 'string',
                'count': 'int'
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
}

FETCH_UPLOAD_RESPONSE = {
    '200': openapi.Response(
        description='User has successfully fetched their eye image upload',
        examples={
            'application/json': {
                'message': 'Done',
                'upload': {
                    'id': 0,
                    'uuid': 'string',
                    'description': 'string',
                    'images': ['url']
                }
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
    '403': openapi.Response(
        description='User does not have permission',
        examples={
            'application/json': {
                'message': 'Invalid permissions'
            }
        }
    ),
}

UPDATE_UPLOAD_RESPONSE = {
    '200': openapi.Response(
        description='User has successfully updated their eye image upload',
        examples={
            'application/json': {
                'message': 'Done',
                'upload': {
                    'id': 0,
                    'uuid': 'string',
                    'description': 'string',
                    'images': ['url']
                }
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
    '403': openapi.Response(
        description='User does not have permission',
        examples={
            'application/json': {
                'message': 'Invalid permissions'
            }
        }
    ),
}

DELETE_UPLOAD_RESPONSE = {
    '200': openapi.Response(
        description='User has successfully deleted the eye image uploads',
        examples={
            'application/json': {
                'message': 'Done'
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
    '403': openapi.Response(
        description='User does not have permission',
        examples={
            'application/json': {
                'message': 'Invalid permissions'
            }
        }
    ),
}

FETCH_UPLOADS_RESULTS_RESPONSE = {
    '200': openapi.Response(
        description='User has successfully deleted the eye image uploads',
        examples={
            'application/json': {
                'message': 'Done',
                'xray_upload': {},
                'results': []
            }
        }
    ),
    '401': openapi.Response(
        description='User is not authenticated',
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
    '403': openapi.Response(
        description='User does not have permission',
        examples={
            'application/json': {
                'message': 'Invalid permissions'
            }
        }
    ),
}
