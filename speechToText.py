import requests
import base64
import json

key = "AIzaSyD_FSi4MxStTxYnUrYAupe9SwPcy0Zx96s"

url = "https://speech.googleapis.com/v1beta1/speech:syncrecognize?key="+key
print(url) 
# encoding audio file with Base64 (~200KB, 15 secs)
with open("output.flac", 'rb') as speech:
    speech_content = base64.b64encode(speech.read())

payload = { 
    'initialRequest': {
        'encoding': 'FLAC',
        'sampleRate': 16000,
    },
    'audioRequest': {
        'content': speech_content.decode('UTF-8'),
    },
}

# POST request to Google Speech API
r = requests.post(url, data=json.dumps(payload))
print(r.content)