import wave
from pydub import AudioSegment
import speech_recognition as sr

def convert_mp3_to_wav(path) : 

    audio = AudioSegment.from_mp3(path)
    file_name = path.split('.')[0]
    path = f'{file_name}.wav'

    audio.export(path , format = 'wav')

    return path


def get_transcriptions(path) :

    recognizer = sr.Recognizer() 

    with sr.AudioFile(path) as source : audio = recognizer.record(source)

    try : text = recognizer.recognize_google(audio)
    except sr.UnknownValueError : text = ''

    return text

def audio_to_text(path) : 

    if path.endswith('mp3') : path = convert_mp3_to_wav(path)

    wf = wave.open(path , 'rb')

    transcription = get_transcriptions(path)

    return transcription