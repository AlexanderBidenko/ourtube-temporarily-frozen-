import os
import subprocess
from gtts import gTTS
import wave
from pytube import YouTube
from string_processing import list_of_transleted_phrases as lotp
from string_processing import time_codes
from string_processing import lineal_string


youtube_video_url = 'https://www.youtube.com/watch?v=G0aekmshR4A'
def time_for_framerate(file):
    list_of_time = [0]
    time = 0
    tc = time_codes(file)
    for i in range(1, len(tc)):
        time = int(tc[i][0] + tc[i][1])*60 + int(tc[i][3] + tc[i][4]) - (int(tc[i-1][0] + tc[i-1][1])*60 + int(tc[i-1][3] + tc[i-1][4]))
        list_of_time.append(time)
    list_of_time.append(2)
    return list_of_time


file = "file.txt"
list_of_time = time_for_framerate(file)
list_of_phrases = lotp(file)
yt_obj = YouTube(youtube_video_url)
len_vid = yt_obj.length
print(type(len_vid))

language = "ru"
text = lineal_string(file)
title = 'converted_to_wav_file.wav'
speech = gTTS(text=text, lang=language, slow=False)
speech.save(title)
subprocess.call(['ffmpeg', '-i', title,
                 'converted_to_wav_file.wav'])
"""source = wave.open("converted_to_wav_file.wav", mode="wb")
source.setparams(source.getparams())
source.setframerate((source.getnframes()) // len_vid)
source.close()

for i in range(1, len(list_of_phrases)):
    text = list_of_phrases[i]
    language = "ru"

    speech = gTTS(text=text, lang=language, slow=False)
    title = str(i)
    speech.save(title)

    # convert mp3 to wav file
    source = wave.open("converted_to_wav_file.wav", mode="rb")
    audio = wave.open((title + "output.wav"), mode="wb")
    audio.setparams(source.getparams())
    print(source.getnframes())
    audio.setframerate((source.getnframes())/(list_of_time[i]))
    audio.writeframes(source.readframes(source.getnframes()))

    source.close()
    audio.close()

    os.remove("./converted_to_wav_file.wav")
    os.remove("./" + str(i))"""
