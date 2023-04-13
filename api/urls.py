from .views import CaptionImageUploadView
from django.urls import path

urlpatterns = [
    path('v1/caption', CaptionImageUploadView.as_view(), name='caption'),
]
