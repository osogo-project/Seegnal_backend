from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CaptionImageSerializer, OCRImageSerializer
from googletrans import Translator
from tempfile import NamedTemporaryFile
import os
import replicate
import requests
import uuid
import time
import json


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
                input={
                    "image": open(image_path, 'rb'),
                    "model": "conceptual-captions",
                    "use_beam_search": True
                }
            )
            trans_output = translator.translate(
                output, src='en', dest='ko'
            ).text
            return Response({'text': trans_output}, status=201)
        else:
            return Response({'text': 'error'}, status=400)


api_url = 'https://apdgtp42qg.apigw.ntruss.com/custom/v1/22739/5eff5c5d0f49882e4cd18e77793f0799d7650aecb26e4e6c7502fffd99557947/general'
secret_key = 'QU9ncHF2ZEZlZFlZS3RjSml3dHZDRmthYUdaSXhzdXo='


class OCRKRView(APIView):
    def post(self, request):
        serializer = OCRImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            image_path = convert_uploaded_file_to_path(image)

            request_json = {
                'images': [
                    {
                        'format': 'jpg',
                        'name': 'demo'
                    }
                ],
                'requestId': str(uuid.uuid4()),
                'version': 'V2',
                'timestamp': int(round(time.time() * 1000))
            }

            payload = {'message': json.dumps(request_json).encode('UTF-8')}
            files = [
                ('file', open(image_path, 'rb'))
            ]
            headers = {
                'X-OCR-SECRET': secret_key
            }

            response = requests.request(
                "POST", api_url, headers=headers, data=payload, files=files)

            result = response.text.encode('utf8')
            result_json = json.loads(result.decode('utf8').replace("'", '"'))
            result_fields = result_json['images'][0]['fields']

            result_list = []
            for result_field in result_fields:
                result_list.append(result_field['inferText'])

            result_text = ' '.join(result_list)

            return Response({'text': result_text}, status=201)
        else:
            return Response({'text': 'error'}, status=400)
