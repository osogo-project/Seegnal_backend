from .views import CaptionImageUploadView, CaptionImageUploadENView, ImageCaptioningKRView, ImageCaptioningENView
from django.urls import path

urlpatterns = [
    path('v1/caption', CaptionImageUploadView.as_view(), name='caption'),
    path('v1/caption_en', CaptionImageUploadENView.as_view(), name='caption_en'),
    path('v2/caption_kr', ImageCaptioningKRView.as_view()),
    path('v2/caption_en', ImageCaptioningENView.as_view()),
]
