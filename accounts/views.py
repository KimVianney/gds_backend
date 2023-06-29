from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


from . import user_crud
from .docs import request_body, responses

# Create your views here.

class UserCreateAPIView(APIView):

    @swagger_auto_schema(
        request_body=request_body.REGISTER_USER_SCHEMA,
        responses=responses.REGISTER_USER_RESPONSES,
        security=[],
        operation_id='Register a user',
        operation_description='Register a user',
    )
    def post(self, request):
        return user_crud.create(request)

class LoginAPIView(APIView):

    @swagger_auto_schema(
        request_body=request_body.LOGIN_USER_SCHEMA,
        responses=responses.LOGIN_USER_RESPONSES,
        security=[],
        operation_id='Log in a user',
        operation_description='Log in a user',
    )
    def post(self, request):
        return user_crud.login_user(request)

class UserRetrieveUpdateDeleteAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        responses=responses.GET_USER_DETAILS_RESPONSE,
        operation_id='Get a users details',
        operation_description='Get a users details',
    )
    def get(self, request):
        return user_crud.get(request)

    @swagger_auto_schema(
        request_body=request_body.UPDATE_USER_SCHEMA,
        responses=responses.UPDATE_USER_DETAILS_RESPONSE,
        operation_id='Update a user',
        operation_description='Update a user',
    )
    def put(self, request):
        return user_crud.update(request)

    @swagger_auto_schema(
        responses=responses.DELETE_USER_RESPONSE,
        operation_id='Delete a user',
        operation_description='Delete a user',
    )
    def delete(self, request):
        return user_crud.delete(request)