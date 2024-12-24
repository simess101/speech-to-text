from rest_framework.views import APIView
from rest_framework.response import Response
import whisper

class SpeechToText(APIView):
    def post(self, request):
        audio_file = request.FILES['audio']
        model = whisper.load_model("base")
        result = model.transcribe(audio_file.temporary_file_path())
        return Response({"transcription": result['text']})
