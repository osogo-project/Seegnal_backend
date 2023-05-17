from .views import ImageCaptioningKRView, ImageCaptioningENView
from django.urls import path

urlpatterns = [
    path('v2/caption_kr', ImageCaptioningKRView.as_view(), name='caption_kr'),
    path('v2/caption_en', ImageCaptioningENView.as_view(), name='caption_en'),
]
