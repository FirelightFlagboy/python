# -*- coding: utf-8 -*-

from pydub import AudioSegment

FILE_NAME = "Benny Goodman - Sing Sing Sing"
FILE_M4A = FILE_NAME + ".m4a"
FILE_MP3 = FILE_NAME + "mp3"
wav_audio = AudioSegment.from_file("audio.wav", format="wav")
raw_audio = AudioSegment.from_file("audio.wav", format="raw",
								   frame_rate=44100, channels=2, sample_width=2)

wav_audio.export("audio1.mp3", format="mp3")
raw_audio.export("audio2.mp3", format="mp3")
flac_audio = AudioSegment.from_file(FILE_M4A, "flac")
flac_audio.export(FILE_MP3, format="mp3")
