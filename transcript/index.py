import openai
import json
import datetime
openai.api_key = "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"

audio_file= open("witze/Dennis.wav", "rb")
#openai.Audio.detect_language = "Chinese"
openai.Audio.response_format="srt"
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript.text)


# Initialize the SRT counter and timestamp
srt_counter = 1
srt_timestamp = datetime.timedelta(seconds=0)


srt = ""
for i, item in enumerate(data):
    srt += str(i+1) + "\n"
    srt += item['start_time'] + " --> " + item['end_time'] + "\n"
    srt += item['text'] + "\n\n"
