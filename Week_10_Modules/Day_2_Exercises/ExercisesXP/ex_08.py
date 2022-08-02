"""
Exercise 8 : How Old Are You On Jupiter?
Instructions
Given an age in seconds, calculate how old someone would be on:
Earth: orbital period 365.25 Earth days, or 31557600 seconds
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years
So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.
"""

earth_orbital_seconds = 31557600

planets = {
    'Earth': earth_orbital_seconds,
    'Mercury': earth_orbital_seconds / 0.2408467,
    'Venus': earth_orbital_seconds / 0.61519726,
    'Mars': earth_orbital_seconds * 1.8808158,
    'Jupiter': earth_orbital_seconds * 11.862615,
    'Saturn': earth_orbital_seconds * 29.447498,
    'Uranus': earth_orbital_seconds * 84.016846,
    'Neptune': earth_orbital_seconds *164.79132
}


def age_on_planet(age_seconds):
    for planet, orbital_seconds in planets.items():
        age_years = round(age_seconds / orbital_seconds, 2)
        print(f'{planet}: {age_years} years.')


age_on_planet(1000000000)