import json

family = None
with open('file.json') as f:
    family = json.load(f)

print(family['children'])

family['children'][0]['favorite_color'] = 'blue'
family['children'][1]['favorite_color'] = 'black'
print(family['children'])

with open('file.json', mode='w') as f:
    json.dump(family, f, indent=2)

