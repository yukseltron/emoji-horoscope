import requests

params = (
('sign', 'aries'),
('day', 'today'),
)

r = requests.post('https://aztro.sameerkumar.website/', params=params)

print(r.status_code)
print(r.status_code == requests.codes.ok)

data = r.json()
print(data['description'])
