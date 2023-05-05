import openai
openai.api_key = "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"


audio_file= open("STE.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
