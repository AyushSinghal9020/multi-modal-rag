import wave
import json

from pydub import AudioSegment
import speech_recognition as sr
from moviepy.editor import VideoFileClip

def extract_audio_from_video(path) : 

    video = VideoFileClip(path)

    audio = video.audio

    if not audio : return 'No Audio'
        
    audio.write_audiofile('audio.wav')

    path = 'audio.wav'

    return path

def get_transcriptions(path) : 

    recognizer = sr.Recognizer() 

    wf = wave.open(path , 'rb')

    with sr.AudioFile(path) as source : audio = recognizer.record(source)

    try : text = recognizer.recognize_google(audio)
    except sr.UnknownValueError : text = ''

    return text

def video_to_text(path) : 

    path = extract_audio_from_video(path)

    if path == 'No Audio' : return 'Couldnt Extract Audio form the Video'

    wf = wave.open(path , 'rb')

    transcription = get_transcriptions(path)

    return transcription