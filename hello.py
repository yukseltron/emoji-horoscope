import json
import requests
import random
from watson_developer_cloud import ToneAnalyzerV3


params = (
('sign', 'aries'),
('day', 'today'),
)


def getScope(params):
    r = requests.post('https://aztro.sameerkumar.website/', params=params)
    data = r.json()

    return data


def getTone(data):
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='xakWAE0E92YVWWnzf5rYgOLKZcJb5kecM_zINqqLKZCY',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )

    tone_analysis = tone_analyzer.tone(
        {'text': data},
        'application/json'
    ).get_result()

    return tone_analysis

def joy():
    joy = ['😁','😀','😂','😆','🤑','🤣','😊','😋','😍','😇']
    return joy[random.randrange(10)]

def anger():
    joy = ['😡','🤬','😠','🤯','👺','😤']
    return anger[random.randrange(6)]

def fear():
    joy = ['😱','😰','😨','😬','😳','😥']
    return fear[random.randrange(6)]

def sadness():
    joy = ['☹️','😖','😞','😢','😭','😕','🙃','😔']
    return sadness[random.randrange(8)]

def analytical():
    joy = ['🤔','🤨','🧐']
    return analytical[random.randrange(3)]

def confident():
    joy = ['😛','😜','😏']
    return confident[random.randrange(3)]

def tentative():
    joy = ['😒','😑','😓','😶']
    return joy[random.randrange(4)]

def getEmoji(tone):
    switcher = {
        'joy': joy(),
        'anger': "February",
        'fear': "March",
        'sadness': "May",
        'analytical': "June",
        'confident': "July",
        'tentative': "August"
    }
    print(switcher.get(tone, "Invalid month"))

def analyzeScope():
    data = getScope(params)
    tone = getTone(data['description'])
    emotionalTone = tone['document_tone']['tones'][0]['tone_id']
    languageTone = tone['document_tone']['tones'][1]['tone_id'] #test for only 1 tone
    getEmoji(emotionalTone)

analyzeScope()
