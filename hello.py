import json
import requests
from watson_developer_cloud import ToneAnalyzerV3


params = (
('sign', 'taurus'),
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


def analyzeScope():
    data = getScope(params)
    tone = getTone(data['description'])
    emotionalTone = tone['document_tone']['tones'][0]['tone_id']
    languageTone = tone['document_tone']['tones'][1]['tone_id']

    print(languageTone)

analyzeScope()
