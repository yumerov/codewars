# https://www.codewars.com/kata/directions-reduction/train/python
from unittest import TestCase


def dirReduc(arr):
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }
    reduced_direction = []
    for direction in arr:
        opposite = opposites[direction]
        last = reduced_direction[-1] if reduced_direction else None
        if last == opposite:
            reduced_direction.pop()
        else:
            reduced_direction.append(direction)

    return reduced_direction


test = TestCase()
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assertEqual(dirReduc(a), ['WEST'])
u = ["NORTH", "WEST", "SOUTH", "EAST"]
test.assertEqual(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
b = ['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']
test.assertEqual(dirReduc(b), ['EAST', 'NORTH'])