from rest_framework import serializers

from .models import ImageUpload, UploadResult


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        read_only_fields = ('created_at', 'updated_at')
        fields = ('id', 'uuid', 'description', 'images', 'created_at', 'updated_at')
        user = serializers.ReadOnlyField()

class CreateUploadResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadResult
        fields = ('id', 'image', 'image_class', 'results')
        image_upload = serializers.ReadOnlyField()


class UploadResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadResult
        fields = ('id', 'image', 'image_class', 'results', 'result_image', 
                  'created_at', 'updated_at')

        results = serializers.SerializerMethodField('get_upload_results')

    def get_upload_results(self, obj):
        return obj.uploadResults
    
class ImageResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadResult
        fields = '__all__'
        