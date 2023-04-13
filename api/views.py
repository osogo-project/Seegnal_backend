import os
import json
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import CaptionImageSerializer
from googletrans import Translator
from gtts import gTTS
import replicate

translator = Translator()

os.environ["REPLICATE_API_TOKEN"] = "e703f82f0d7127588a4bd85d57284c3acb192ae5"


class CaptionImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = CaptionImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            output = replicate.run(
                "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
                input={"image": open(f'{serializer.data["image"][1:]}', 'rb')}
            )  # time : 2.69s
            trans_output = translator.translate(
                output, src='en', dest='ko'
            ).text
            # time : 3.79s

            # sp = gTTS(lang='ko', text=trans_output, slow=False)
            # audio_file = f'media/sph/{serializer.data["id"]}.mp3'
            # sp.save(audio_file)
            # # time : 16.65s

            return Response({'text': trans_output}, status=201)
        else:
            return Response(serializer.errors, status=400)


def caption_view(request):
    serializer = CaptionImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # Run the image through the model
        # output = replicate.run(
        #     "rmokady/clip_prefix_caption:9a34a6339872a03f45236f114321fb51fc7aa8269d38ae0ce5334969981e4cd8",
        #     input={"image": open(f'{serializer.data["image"]}', 'rb')}
        # )
        # print(output)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # # Convert the output text to audio
    # sp = gTTS(lang='en', text=output, slow=False)
    # audio_file = 'image_caption.mp3'
    # sp.save(audio_file)

    return Response({'error': 'No image file provided.'}, status=400)
