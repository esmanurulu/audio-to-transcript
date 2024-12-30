from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import wave
import json


audio_file_path = "/Users/esmanurulu/Downloads/Yeni Kayıt 4.m4a"  #ses dosyası
wav_file_path = "/Users/esmanurulu/Desktop/Yeni_Kayıt_4.wav"  #wav dosyası

audio = AudioSegment.from_file(audio_file_path)
audio.export(wav_file_path, format="wav")

# Vosk modelini yükle ve transkripsiyon yap
model_path = "/Users/esmanurulu/Desktop/vosk-model-small-tr-0.3"  # turkish vosk model
model = Model(model_path)

wf = wave.open(wav_file_path, "rb")
recognizer = KaldiRecognizer(model, wf.getframerate())

transcription = ""
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        transcription += result.get("text", "") + " "

result = json.loads(recognizer.FinalResult())
transcription += result.get("text", "")

# transkripti terminale bas
print("transkript:")
print(transcription.strip())

#file'a transkkripti yaz
with open("transcription.txt", "w", encoding="utf-8") as file:
    file.write(transcription.strip())
