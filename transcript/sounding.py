import os
import random
from translate import Translator
import time
import openai
import json
import datetime
openai.api_key = "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"
from playsound import playsound

import os, glob

def first2(s):
    return s[:2]
text = '''Agnes en_US
Alex  en_US
Alice it_IT
Alva  sv_SE
Amelie    fr_CA
Anna  de_DE
Carmit    he_IL
Damayanti id_ID
Daniel    en_GB
Diego es_AR
Ellen nl_BE
Fiona en-scotland
Fred  en_US
Ioana ro_RO
Joana pt_PT
Kanya th_TH
Karen en_AU
Kyoko ja_JP
Laura sk_SK
Lekha hi_IN
Luciana   pt_BR
Maged ar_SA
Mariska   hu_HU
Mei-Jia   zh_TW
Melina    el_GR
Milena    ru_RU
Moira en_IE
Monica    es_ES
Nora  nb_NO
Paulina   es_MX
Samantha  en_US
Sara  da_DK
Satu  fi_FI
Sin-ji    zh_HK
Tessa en_ZA
Thomas    fr_FR
Ting-Ting zh_CN
Veena en_IN
Victoria  en_US
Xander    nl_NL
Yelda tr_TR
Yuna  ko_KR
Zosia pl_PL
Zuzana    cs_CZ'''
temp = text.split('\n')
#print(temp)

language = {}

for i in temp:
    k = i.split(' ')
    k[:] = [item for item in k if item != '']
    #print(k)
    language[k[0]] = k[1]


fileNames = []
path = 'witze/'
for filename in glob.glob(os.path.join(path, '*.wav')):
    fileNames.append(filename)


choiceFile = random.choice(fileNames)
print(choiceFile)
audio_file= open(choiceFile, "rb")
#openai.Audio.detect_language = "Chinese"
#openai.Audio.response_format="srt"
transcript = openai.Audio.transcribe("whisper-1", audio_file)

transcription = (transcript.text)
print(transcription)

os.system("play "+choiceFile+"&") 
time.sleep(5)

for k in range(100):
    pick = random.choice(list(language.keys()))
    translator= Translator(to_lang=first2(language[pick]))
    #input_text = "Was ist erst grün und dann rot? Ein Frosch im Mixer."
    input_text = transcription
    output = translator.translate(input_text)

    os.system("say -v "+pick+" '"+output+"' &") 
