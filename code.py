!pip install SpeechRecognition pydub
!apt install ffmpeg

from google.colab import files
uploaded = files.upload()

import speech_recognition as sr
from pydub import AudioSegment

# Convert MP3 to WAV if needed
sound = AudioSegment.from_file("voice.mp3")  # or your file name
sound.export("converted.wav", format="wav")

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio
with sr.AudioFile("converted.wav") as source:
    audio = recognizer.record(source)

# Convert speech to text
try:
    text = recognizer.recognize_google(audio)
    print("Transcription:")
    print(text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print(f"Error from Google API: {e}")
