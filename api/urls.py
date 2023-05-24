from .views import ImageCaptioningKRView, OCRKRView
from django.urls import path

urlpatterns = [
    path('v2/caption_kr', ImageCaptioningKRView.as_view(), name='caption_kr'),
    path('v2/ocr_kr', OCRKRView.as_view(), name='ocr_kr'),
]
