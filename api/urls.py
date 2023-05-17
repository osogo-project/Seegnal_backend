from .views import CaptionImageUploadView, CaptionImageUploadENView, ImageCaptioningKRView, ImageCaptioningENView
from django.urls import path

urlpatterns = [
    path('v1/caption', CaptionImageUploadView.as_view(), name='caption'),
    path('v1/caption_en', CaptionImageUploadENView.as_view(), name='caption_en'),
]
