from rest_framework import status
from rest_framework.response import Response

from .models import UploadResult, ImageUpload
from .paginators import ImageUploadPagination
from .serializers import UploadResultSerializer, ImageUploadSerializer
from .tasks import get_image_upload_results
from .validators import (validate_create_image_upload,
                         validate_update_image_upload)


def create(request):
    """
    Upload an image
    """
    result = validate_create_image_upload(request.data)
    if result:
        response = {
            'message': 'Invalid values',
            'error': result
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    serializer = ImageUploadSerializer(data=request.data)
    if not serializer.is_valid():
        response = {'message': 'Invalid values', 'error': serializer.errors}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    serializer.save(user=request.user)
    get_image_upload_results.delay(serializer.data['id'])

    response = {'message': 'Done', 'upload': serializer.data}
    return Response(response, status=status.HTTP_201_CREATED)

def get(request):
    """
    Get all a users eye image uploads
    """
    uploads = ImageUpload.objects.filter(
        user__id=request.user.id
    ).order_by('-updated_at')

    paginator = ImageUploadPagination()
    results = paginator.paginate_queryset(uploads, request)

    serializer = ImageUploadSerializer(results, many=True)
    # serializer.is_valid()
        
    response = paginator.get_paginated_response(serializer.data)
    return Response(response, status=status.HTTP_200_OK)

def is_upload(upload):
    """
    Check if the upload is not a None value
    """

    if not upload:
        response = {'message': 'Invalid image upload ID'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    return None

def update(upload, request):
    """
    Update an image description
    """
    if response := is_upload(upload):
        return response

    result = validate_update_image_upload(request.data)
    if result:
        response = {'message': 'Invalid values', 'error': result}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    upload.description = request.data['descripton']
    upload.save()

    serializer = ImageUploadSerializer(upload)

    response = {'message': 'Done!', 'upload': serializer.data}
    return Response(response, status=status.HTTP_200_OK)

def get_upload(upload):
    """
    Get an upload
    """
    if response := is_upload(upload):
        return response

    serializer = ImageUploadSerializer(upload)

    response = {'message': 'Done!', 'upload': serializer.data}
    return Response(response, status=status.HTTP_200_OK)

def delete(upload):
    """
    Delete an x-ray upload and its related results
    """
    if response := is_upload(upload):
        return response

    upload.delete()

    response = {'message': 'Done!'}
    return Response(response, status=status.HTTP_200_OK)

def get_results(image_upload):
    if response := is_upload(image_upload):
        return response

    image_serializer = ImageUpload(image_upload)

    results = UploadResult.objects.filter(image_upload__id=image_upload.id)
    results_serializer = UploadResultSerializer(results, many=True)

    response = {
        'message': 'Done!',
        'image_upload': image_serializer.data,
        'results': results_serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)

