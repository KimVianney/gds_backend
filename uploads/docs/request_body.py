from drf_yasg import openapi

CREATE_UPLOAD_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'uuid': openapi.Schema(title='UUID', description='UUID identifying the uploads', type=openapi.TYPE_STRING),
        'description': openapi.Schema(title='Description', description='Description for the uploads', type=openapi.TYPE_STRING),
        'images': openapi.Schema(title='Images', description='Images of the uploads', type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING),
    }
)

UPDATE_UPLOAD_SCHEMA = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'description': openapi.Schema(title='Description', description='Description for the uploads', type=openapi.TYPE_STRING)
    }
)
