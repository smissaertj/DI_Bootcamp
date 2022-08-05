import json
from pyowm.utils import timestamps
from pyowm.owm import OWM

with open('config.json', mode='r') as config_file:
    config = json.load(config_file)

api_key = config['api_key']

owm = OWM(api_key)
city_registry = owm.city_id_registry()

# list_of_tuples = telaviv = city_registry.ids_for('tel aviv', matching='like')
# print(list_of_tuples)
# [(293396, 'Tel Aviv District', 'IL', None, 32.083328, 34.799999), (293397, 'Tel Aviv', 'IL', None, 32.080879, 34.780571)]

mgr = owm.weather_manager()


# observation = mgr.weather_at_place('Tel Aviv,IL')
#
# # Get current weather in Tel Aviv
# current_weather_status = observation.weather.detailed_status
#
# # Get current wind speed in meters per second.
# current_wind_speed = observation.weather.wind()['speed']
#
# # Get sunsrise/sunset time in UTC
# sunrise_time = observation.weather.sunrise_time(timeformat='iso')
# sunset_time = observation.weather.sunset_time(timeformat='iso')
#
#
# print(f'The current weather in Tel Aviv, Isreal: {current_weather_status}.\n'
#       f'The wind is blowing at {current_wind_speed} meters per second.\n'
#       f'Sunrise was at {sunrise_time} UTC\n'
#       f'Sunset was at {sunset_time} UTC.\n')


location = input('Enter the name of a city: ')
result = city_registry.ids_for(location, matching='like')

for city in result:
    print(f'ID: {city[0]} - Name: {city[1]} - Country: {city[2]}')

city_id = int(input('Enter City ID: '))

observation = mgr.weather_at_id(city_id)
current_weather_status = observation.weather.detailed_status
current_wind_speed = observation.weather.wind()['speed']
sunrise_time = observation.weather.sunrise_time(timeformat='iso')
sunset_time = observation.weather.sunset_time(timeformat='iso')

print(f'\nThe current weather in {location}: {current_weather_status}.\n'
      f'The wind is blowing at {current_wind_speed} meters per second.\n'
      f'Sunrise was at {sunrise_time} UTC\n'
      f'Sunset was at {sunset_time} UTC.\n')

daily_forecast = mgr.forecast_at_id(city_id, '3h')
tomorrow = timestamps.tomorrow()
weather = daily_forecast.get_weather_at(tomorrow)

print(f'The weather for tommorow will be {weather.detailed_status}.')



