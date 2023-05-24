from rest_framework import serializers
from .models import CaptionImage, OCRImage


class CaptionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptionImage
        fields = '__all__'


class OCRImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OCRImage
        fields = '__all__'
