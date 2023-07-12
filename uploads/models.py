import json

from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

User = get_user_model()

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ImageUpload(TimestampMixin, models.Model):
    uuid = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=False, blank=False)
    images = ArrayField(models.URLField())
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'image_uploads'
        verbose_name = 'Eye Image Uploads'
        verbose_name_plural = 'Eye Image Uploads'


class UploadResult(TimestampMixin, models.Model):
    image_upload = models.ForeignKey(ImageUpload, on_delete=models.CASCADE)
    image = models.URLField(blank=True)
    image_class = models.CharField(max_length=100)
    results = models.TextField()

    class Meta:
        db_table = "image_upload_results"
        verbose_name = "Image Upload Results"
        verbose_name_plural = "Image Upload Results"

    @property
    def uploadResults(self):
        return json.loads(self.results)
