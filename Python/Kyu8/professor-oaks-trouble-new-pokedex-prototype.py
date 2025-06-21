# https://www.codewars.com/kata/professor-oaks-trouble-new-pokedex-prototype/train/python

from unittest import TestCase

class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def get_level(self):
        if self.level <= 20:
            return "weak"

        if self.level <= 50:
            return "fair"

        return "strong"

    def get_type(self):
        if self.pkmntype == "water":
            return "wet"

        if self.pkmntype == "fire":
            return "fiery"

        if self.pkmntype == "grass":
            return "grassy"

        return self.pkmntype

    def info(self):
        return "{}, a {} and {} Pokemon.".format(self.name, self.get_type(),
                                                self.get_level())

test = TestCase()
t = test.assertEqual
t(PokeScan('Squirtle', 0, 'water').info(), 'Squirtle, a wet and weak Pokemon.')
t(PokeScan('Charmander', 0, 'fire').info(), 'Charmander, a fiery and weak Pokemon.')
t(PokeScan('Bulbasaur', 0, 'grass').info(), 'Bulbasaur, a grassy and weak Pokemon.')

t(PokeScan('Squirtle', 20, 'water').info(), 'Squirtle, a wet and weak Pokemon.')
t(PokeScan('Charmander', 20, 'fire').info(), 'Charmander, a fiery and weak '
                                             'Pokemon.')
t(PokeScan('Bulbasaur', 20, 'grass').info(), 'Bulbasaur, a grassy and weak '
                                             'Pokemon.')

t(PokeScan('Squirtle', 21, 'water').info(), 'Squirtle, a wet and fair Pokemon.')
t(PokeScan('Charmander', 21, 'fire').info(), 'Charmander, a fiery and fair '
                                             'Pokemon.')
t(PokeScan('Bulbasaur', 21, 'grass').info(), 'Bulbasaur, a grassy and fair '
                                             'Pokemon.')

t(PokeScan('Squirtle', 50, 'water').info(), 'Squirtle, a wet and fair '
                                             'Pokemon.')
t(PokeScan('Charmander', 50, 'fire').info(), 'Charmander, a fiery and fair '
                                             'Pokemon.')
t(PokeScan('Bulbasaur', 50, 'grass').info(), 'Bulbasaur, a grassy and fair '
                                             'Pokemon.')

test.assertEqual(PokeScan('Squirtle', 51, 'water').info(), 'Squirtle, a wet and strong Pokemon.')
test.assertEqual(PokeScan('Charmander', 51, 'fire').info(), 'Charmander, a fiery and strong Pokemon.')
test.assertEqual(PokeScan('Bulbasaur', 51, 'grass').info(), 'Bulbasaur, a grassy and strong Pokemon.')

test.assertEqual(PokeScan('Squirtle', 100, 'water').info(), 'Squirtle, a wet and strong Pokemon.')
test.assertEqual(PokeScan('Charmander', 100, 'fire').info(), 'Charmander, a fiery and strong Pokemon.')
test.assertEqual(PokeScan('Bulbasaur', 100, 'grass').info(), 'Bulbasaur, a grassy and strong Pokemon.')
