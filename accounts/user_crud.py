from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializer
from .validators import validate_register_user, validate_update_user_details


def create(request):
    """
    Create a user
    """
    result = validate_register_user(request.data)
    if result is not None:
        response = {'message': 'Invalid values', 'error': result}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data, many=True)
    if not serializer.is_valid():
        response = {'message': 'Invalid values', 'error': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    user = serializer.instance
    token = user.get_access_token

    response = {'message': 'Done!', 'user': serializer.data, **token}
    return Response(response, status=status.HTTP_201_CREATED)