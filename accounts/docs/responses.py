from drf_yasg import openapi


REGISTER_USER_RESPONSES = {
    '201': openapi.Response(
        description='User successfully registered',
        examples={
            'application/json': {
                'message': 'Done',
                'access': 'access_token',
                'user': {
                    'id': 1,
                    'email': 'string',
                    'first_name': 'string',
                    'last_name': 'string'
                }
            }
        }
    ),
    '400': openapi.Response(
        description='Invalid reuest data',
        examples={
            'application/json': {
                'message': 'Invalid values',
                'error': {}
            }
        }
    )
}

GET_USER_DETAILS_RESPONSE = {
    '200': openapi.Response(
        description='Fetched user details',
        examples={
            'application/json': {
                'message': 'Done',
                'user': {
                    'id': 1,
                    'email': 'string',
                    'first_name': 'string',
                    'last_name': 'string'
                }
            }
        }
    ),
    '401': openapi.Response(
        description='Not authenticated',
        examples={
            'application/json': {
                'message': 'Not authorized'
            }
        }
    )
}

UPDATE_USER_DETAILS_RESPONSE = {
    '200': openapi.Response(
        description='Updated user details',
        examples={
            'application/json': {
                'message': 'Done',
                'user': {
                    'id': 1,
                    'email': 'string',
                    'first_name': 'string',
                    'last_name': 'string'
                }
            }
        }
    ),
    '400': openapi.Response(
        description='Invalid values',
        examples={
            'application/json': {
                'message': 'Invalid values',
                'error': {}
            }
        }
    ),
    '401': openapi.Response(
        description='Not authenticated',
        examples={
            'application/json': {
                'message': 'Not authorized'
            }
        }
    )
}

DELETE_USER_RESPONSE = {
    '200': openapi.Response(
        description='Deleted user',
        examples={
            'application/json': {
                'message': 'Done'
            }
        }
    ),
    '401': openapi.Response(
        description='Not authenticated',
        examples={
            'application/json': {
                'message': 'Not authorized'
            }
        }
    )
}

LOGIN_USER_RESPONSES = {
    '200': openapi.Response(
        description='User successfully logged in',
        examples={
            'application/json': {
                'message': 'Done',
                'access': 'access_token',
                'user': {
                    'id': 1,
                    'email': 'string',
                    'first_name': 'string',
                    'last_name': 'string'
                }
            }
        }
    ),
    '400': openapi.Response(
        description='Invalid credentials',
        examples={
            'application/json': {
                'message': 'Invalid credentials'
            }
        }
    )
}
