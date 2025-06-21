# https://www.codewars.com/kata/simple-pig-latin/train/python
from unittest import TestCase

def transform_word(word): return word[1:] + word[0] + "ay" if word.isalpha() else word

def pig_it(text):
    return " ".join(list(map(transform_word, text.split(" "))))
test = TestCase()
test.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
test.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')