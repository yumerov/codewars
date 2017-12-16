# https://www.codewars.com/kata/get-planet-name-by-id/train/python

from unittest import TestCase

def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return planets[id] if id in planets.keys() else ""

test = TestCase()
test.assertEqual(get_planet_name(2), 'Venus')
test.assertEqual(get_planet_name(5), 'Jupiter')
test.assertEqual(get_planet_name(3), 'Earth')
test.assertEqual(get_planet_name(4), 'Mars')
test.assertEqual(get_planet_name(8), 'Neptune')
test.assertEqual(get_planet_name(1), 'Mercury')