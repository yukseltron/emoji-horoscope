import json
import requests
import random
from watson_developer_cloud import ToneAnalyzerV3


params = (
('sign', 'libra'),
('day', 'today'),
)


#Gets horoscope info
def getScope(params):
    r = requests.post('https://aztro.sameerkumar.website/', params=params)
    data = r.json()
    return data


#Performs tone anlysis
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

def getSign(sign):
    switcher = {
        'Aries': '♈️',
        'Taurus': '♉️',
        'Gemini': '♊️',
        'Cancer': '♋️ ',
        'Leo': '♌️',
        'Virgo': '♍️',
        'Libra': '♎️',
        'Scorpio': '♏️',
        'Sagittarius': '♐️',
        'Capricorn': '♑️',
        'Aquarius': '♒️',
        'Pisces': '♓️'
    }
    return switcher.get(sign)

#switch case to select appropriate emoji
def joy():
    joy = ['😁','😀','😂','😆','🤑','🤣','😊','😋','😍','😇']
    return joy[random.randrange(10)]

def anger():
    anger = ['😡','🤬','😠','🤯','👺','😤']
    return anger[random.randrange(6)]

def fear():
    fear = ['😱','😰','😨','😬','😳','😥']
    return fear[random.randrange(6)]

def sadness():
    sadness = ['☹️','😖','😞','😢','😭','😕','🙃','😔']
    return sadness[random.randrange(8)]

def analytical():
    analytical = ['🤔','🤨','🧐']
    return analytical[random.randrange(3)]

def confident():
    confident = ['😛','😜','😏']
    return confident[random.randrange(3)]

def tentative():
    tentative = ['😒','😑','😓','😶']
    return tentative[random.randrange(4)]

def getEmoji(tone):
    switcher = {
        'joy': joy(),
        'anger': anger(),
        'fear': fear(),
        'sadness': sadness(),
        'analytical': analytical(),
        'confident': confident(),
        'tentative': tentative()
    }
    return switcher.get(tone)


def analyzeScope():
    data = getScope(params) #get the horoscope
    tone = getTone(data['description']) #get the tone of the horoscope
    compatibility = getSign(data['compatibility'])
    emotionalTone = tone['document_tone']['tones'][0]['tone_id'] #get the emotional tone
    finalTone = getEmoji(emotionalTone)

    # Sometimes lanugage tone is unable to be measured
    try:
        languageTone = tone['document_tone']['tones'][1]['tone_id'] #get the language tone
        finalTone += getEmoji(languageTone)
    except:
        pass

    return finalTone + compatibility

print(analyzeScope())
