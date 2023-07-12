from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import upload_crud
from .docs import request_body, responses
from .models import ImageUpload, UploadResult
from .permissions import IsOwner
from .serializers import UploadResultSerializer, ImageResultSerializer

# Create your views here.

class CreateFetchImageUploadsAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        request_body=request_body.CREATE_UPLOAD_SCHEMA,
        responses=responses.CREATE_UPLOAD_RESPONSE,
        operation_id='Add image uploads',
        operation_description='Add image uploads',
    )
    def post(self, request):
        return upload_crud.create(request)

    @swagger_auto_schema(
        responses=responses.FETCH_UPLOADS_RESPONSE,
        operation_id='Fetch image uploads',
        operation_description='Fetch image uploads',
    )
    def get(self, request):
        return upload_crud.get(request)

    
class FetchUpdateDeleteImageUploadsAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_object(self, upload_id):
        try:
            image_upload = ImageUpload.objects.get(pk=upload_id)
            self.check_object_permissions(self.request, image_upload)
            return image_upload
        except ImageUpload.DoesNotExist:
            return None

    @swagger_auto_schema(
        responses=responses.FETCH_UPLOAD_RESPONSE,
        operation_id='Fetch eye image upload',
        operation_description='Fetch image upload',
    )
    def get(self, request, upload_id):
        upload = self.get_object(upload_id)
        return upload_crud.get_upload(request)

    @swagger_auto_schema(
        request_body=request_body.UPDATE_UPLOAD_SCHEMA,
        responses=responses.UPDATE_UPLOAD_RESPONSE,
        operation_id='Update eye image upload',
        operation_description='Update eye image upload',
    )
    def patch(self, request, upload_id):
        upload = self.get_object(upload_id)
        return upload_crud.update(upload, request)

    @swagger_auto_schema(
        responses=responses.DELETE_UPLOAD_RESPONSE,
        operation_id='Delete eye image upload',
        operation_description='Delete eye image upload',
    )
    def delete(self, request, upload_id):
        upload = self.get_object(upload_id)
        return upload_crud.delete(upload)



class FetchImageUploadResultsAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_object(self, upload_id):
        try:
            image_upload = ImageUpload.objects.get(pk=upload_id)
            self.check_object_permissions(self.request, image_upload)
            return image_upload
        except ImageUpload.DoesNotExist:
            return None

    @swagger_auto_schema(
        responses=responses.FETCH_UPLOADS_RESULTS_RESPONSE,
        operation_id='Fetch eye image upload',
        operation_description='Fetch eye image upload',
    )
    def get(self, request, upload_id):
        upload = self.get_object(upload_id)
        return upload_crud.get_results(upload)

class RetrieveUploadResultsAPIView(APIView):
    queryset = UploadResult.objects.all()
    authentication_classes = [JWTAuthentication]
    # lookup_url_kwarg = 'upload_id'
    permission_classes =[permissions.IsAuthenticated, IsOwner]
    serializer_class = ImageResultSerializer
    
    def get_object(self, upload_id):
        try:
            image_upload = ImageUpload.objects.get(pk=upload_id)
            self.check_object_permissions(self.request, image_upload)
            return image_upload
        except ImageUpload.DoesNotExist:
            return None
    
    def get(self, request, upload_id):
        result = UploadResult.objects.filter(image_upload__id=upload_id)
        serializer = ImageResultSerializer(result, many=True)
        return Response(serializer.data, status=200)


    