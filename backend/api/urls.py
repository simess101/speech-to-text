from django.urls import path
from .views import SpeechToText

urlpatterns = [
    path('speech-to-text/', SpeechToText.as_view()),
]
