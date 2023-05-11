import os
import json
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import CaptionImageSerializer
from googletrans import Translator
from tempfile import NamedTemporaryFile
import replicate


def convert_uploaded_file_to_path(file):
    temp_file = NamedTemporaryFile(delete=False)
    temp_file.write(file.read())
    temp_file.close()
    return temp_file.name


translator = Translator()

os.environ["REPLICATE_API_TOKEN"] = "e703f82f0d7127588a4bd85d57284c3acb192ae5"


class ImageCaptioningKRView(APIView):
    def post(self, request):
        serializer = CaptionImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            image_path = convert_uploaded_file_to_path(image)
            output = replicate.run(
                "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
                input={"image": open(image_path, 'rb')}
            )
            trans_output = translator.translate(
                output, src='en', dest='ko'
            ).text
            return Response({'text': trans_output}, status=201)
        else:
            return Response(serializer.errors, status=400)


class ImageCaptioningENView(APIView):
    def post(self, request):
        serializer = CaptionImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            image_path = convert_uploaded_file_to_path(image)
            output = replicate.run(
                "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
                input={"image": open(image_path, 'rb')}
            )
            return Response({'text': output}, status=201)
        else:
            return Response(serializer.errors, status=400)


class CaptionImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = CaptionImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            output = replicate.run(
                "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
                input={"image": open(
                    f'{os.getcwd()}/Seegnal_backend/{serializer.data["image"][1:]}', 'rb')}
            )
            trans_output = translator.translate(
                output, src='en', dest='ko'
            ).text

            return Response({'text': trans_output}, status=201)
        else:
            return Response(serializer.errors, status=400)


class CaptionImageUploadENView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = CaptionImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            output = replicate.run(
                "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
                input={"image": open(
                    f'{os.getcwd()}/Seegnal_backend/{serializer.data["image"][1:]}', 'rb')}
            )

            return Response({'text': output}, status=201)
        else:
            return Response(serializer.errors, status=400)
