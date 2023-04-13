from rest_framework import serializers
from .models import CaptionImage


class CaptionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptionImage
        fields = '__all__'
