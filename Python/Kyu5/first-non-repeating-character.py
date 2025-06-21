# https://www.codewars.com/kata/first-non-repeating-character/train/python

from unittest import TestCase


def first_non_repeating_letter(string):
    if len(string) < 2:
        return string

    first = string[0]
    if string.lower().count(first.lower()) > 1:
        return first_non_repeating_letter(string.replace(first, ""))
    else:
        return first


test = TestCase()
test.assertEqual(first_non_repeating_letter('a'), 'a')
test.assertEqual(first_non_repeating_letter('stress'), 't')
test.assertEqual(first_non_repeating_letter('moonmen'), 'e')
#
test.assertEqual(first_non_repeating_letter(''), '')

test.assertEqual(first_non_repeating_letter('abba'), '')
test.assertEqual(first_non_repeating_letter('aa'), '')
#
test.assertEqual(first_non_repeating_letter('~><#~><'), '#')
test.assertEqual(first_non_repeating_letter('hello world, eh?'), 'w')

test.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
test.assertEqual(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')