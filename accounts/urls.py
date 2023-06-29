from django.urls import path

from .views import (
    LoginAPIView,
    UserCreateAPIView,
    UserRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path('user/', UserRetrieveUpdateDeleteAPIView.as_view()),
    path('register/', UserCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]