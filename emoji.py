# -*- coding: utf-8 -*-
import json
import requests
import random
from watson_developer_cloud import ToneAnalyzerV3
import sys
import importlib
try:
    from google.appengine.api import urlfetch
    from requests_toolbelt.adapters import appengine
    appengine.monkeypatch()
except ImportError:
    pass

if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
#make astrology param to send to api
def setParams(sign):
    params = (
    ('sign', sign),
    ('day', 'today'),
    )
    return params


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

#gets emoji for compatible sign
def getSign(sign):
    switcher = {
        'Aries': '♈️',
        'Taurus': '♉️',
        'Gemini': '♊️',
        'Cancer': '♋️',
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
    anger = ['😡','🤬','😠','🤯','😈','😤']
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
    tentative = ['😒','😑','😓','🤭']
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

def getFaceEmoji():
    emojis = ['😘','😪','😮','🤓','🤤']
    return emojis[random.randrange(5)]

def getRandomEmoji():
    emojis = ['👀','👏','🌞','💩','👅','💦','🌊','🔥','🌟','🐿','🍑','🍆','🎱','🎉']
    return emojis[random.randrange(14)]

def analyzeScope(sign):
    data = getScope(setParams(sign)) #get the horoscope
    tone = getTone(data['description']) #get the tone of the horoscope
    compatibility = getSign(data['compatibility'])
    finalTone = getFaceEmoji() + getFaceEmoji()

    # Sometimes tone is unable to be measured
    try:
        emotionalTone = tone['sentences_tone'][0]['tones'][0]['tone_id'] 
        languageTone = tone['sentences_tone'][0]['tones'][1]['tone_id'] #get the language tone
        finalTone = getEmoji(emotionalTone) + getEmoji(languageTone)
    except IndexError:
        pass
    try:
        emotionalTone = tone['sentences_tone'][0]['tones'][0]['tone_id'] 
        languageTone = tone['sentences_tone'][1]['tones'][0]['tone_id'] #get the language tone
        finalTone = getEmoji(emotionalTone) + getEmoji(languageTone)
    except IndexError:
        pass
    try:
        emotionalTone = tone['sentences_tone'][0]['tones'][0]['tone_id'] 
        languageTone = tone['sentences_tone'][2]['tones'][0]['tone_id'] #get the language tone
        finalTone = getEmoji(emotionalTone) + getEmoji(languageTone)
    except IndexError:
        pass
    try:
        emotionalTone = tone['sentences_tone'][1]['tones'][0]['tone_id'] 
        languageTone = tone['sentences_tone'][1]['tones'][1]['tone_id'] #get the language tone
        finalTone = getEmoji(emotionalTone) + getEmoji(languageTone)
    except IndexError:
        pass
    try:
        emotionalTone = tone['sentences_tone'][1]['tones'][0]['tone_id'] 
        languageTone = tone['sentences_tone'][2]['tones'][0]['tone_id'] #get the language tone
        finalTone = getEmoji(emotionalTone) + getEmoji(languageTone)
    except IndexError:
        pass
    try:
        emotionalTone = tone['sentences_tone'][2]['tones'][0]['tone_id'] 
        languageTone = tone['sentences_tone'][2]['tones'][1]['tone_id'] #get the language tone
        finalTone = getEmoji(emotionalTone) + getEmoji(languageTone)
    except IndexError:
        pass



    return finalTone + compatibility + getRandomEmoji()



#debugging code
#data = getScope(setParams('taurus')) #get the horoscope
#tone = getTone(data['description']) #get the tone of the horoscope
#print(tone['sentences_tone'])
#print(tone['sentences_tone'][1]['tones'][0]['tone_id'])
#print(analyzeScope('taurus'))
