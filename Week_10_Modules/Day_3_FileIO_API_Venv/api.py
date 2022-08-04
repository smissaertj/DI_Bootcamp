import requests

parameters = ''
response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.content)
print(response.text)
print(response.json())
print(response.headers)

# parameters = {"lat": 31.771959, "lon": 35.217018}
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# print(response.text)



response = requests.get('https://api.chucknorris.io/jokes/random')
print(response.json())
print(response.json()['value'])