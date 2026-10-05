
import os
import subprocess
import pyaudio
import json
from vosk import Model, KaldiRecognizer

model = Model(r"C:\Users\Jahan\OneDrive\Desktop\PROJECT ULTRON\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

audio = pyaudio.PyAudio()

stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    input_device_index=3,
    frames_per_buffer=8000
)

stream.start_stream()

print("Listening...")

while True:
    data = stream.read(4000, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result["text"].lower()
        if "calculator" in text:
            print("Opening Calculator...")
            os.system("start calc")

        elif "chrome" in text:
            print("Opening Chrome...")
            os.system('cmd /c "start chrome --profile-directory=Default"')

        elif "brave" in text:
            print("Opening Brave...")
            os.system(r'start "" "C:\Users\jahan\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"')

        elif "spotify" in text:
            print("Opening Spotify...")
            os.system('start spotify:')
        
        elif "play" in text:
            print("detected play command")
            os.system('start spotify:playlist:6Bn0jhXIsLsOfSgJxDaBRw')
            print(text)

        elif "youtube" in text:
            print("Opening YouTube...")
            os.system('start https://www.youtube.com')
        
        elif "code" in text:
            print("Opening VS Code...")
            os.system('start code')

        elif "what" in text:
            print("Opening WhatsApp...")
            os.system(r'start "" explorer.exe shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App')

        elif "clock" in text:
            print("Opening Clock...")
            os.system('start ms-clock:')


        if "wake up" in text:
            print("Jarvis activated")   