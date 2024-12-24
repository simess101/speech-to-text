# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from pydub import AudioSegment
import os
import tempfile
import whisper  # Ensure this imports the correct openai-whisper module


class SpeechToTextView(APIView):
    def post(self, request, format=None):
        if 'audio' not in request.FILES:
            return Response({'error': 'No audio file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        audio_file = request.FILES['audio']
        temp_audio_path = default_storage.save(f"temp/{audio_file.name}", audio_file)
        temp_audio_full_path = os.path.join(default_storage.location, temp_audio_path)

        try:
            # Convert to WAV if necessary
            sound = AudioSegment.from_file(temp_audio_full_path)
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as wav_file:
                sound.export(wav_file.name, format="wav")
                wav_path = wav_file.name

            # Load Whisper model
            model = whisper.load_model("base")  # You can choose 'tiny', 'base', 'small', 'medium', 'large'
            result = model.transcribe(wav_path)
            transcription = result['text']

            # Clean up temporary files
            os.remove(temp_audio_full_path)
            os.remove(wav_path)

            return Response({
                'transcription': transcription,
                'saved_path': temp_audio_full_path
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # Clean up in case of error
            if os.path.exists(temp_audio_full_path):
                os.remove(temp_audio_full_path)
            if 'wav_path' in locals() and os.path.exists(wav_path):
                os.remove(wav_path)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
