from django.urls import path

from .views import (CreateFetchImageUploadsAPIView,
                    FetchUpdateDeleteImageUploadsAPIView,
                    RetrieveUploadResultsAPIView,
                    FetchImageUploadResultsAPIView)

urlpatterns = [
    path('', CreateFetchImageUploadsAPIView.as_view()),
    path('<int:upload_id>/', FetchUpdateDeleteImageUploadsAPIView.as_view()),
    path('<int:upload_id>/results/', RetrieveUploadResultsAPIView.as_view()),
]