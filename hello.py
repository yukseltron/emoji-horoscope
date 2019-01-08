import json
import requests
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    iam_apikey='xakWAE0E92YVWWnzf5rYgOLKZcJb5kecM_zINqqLKZCY',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

params = (
('sign', 'taurus'),
('day', 'today'),
)

r = requests.post('https://aztro.sameerkumar.website/', params=params)

print(r.status_code)
print(r.status_code == requests.codes.ok)

data = r.json()
print(data['description'])

tone_analysis = tone_analyzer.tone(
    {'text': data['description']},
    'application/json'
).get_result()
print(json.dumps(tone_analysis[, indent=2))
