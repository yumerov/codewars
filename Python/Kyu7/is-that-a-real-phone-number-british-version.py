# https://www.codewars.com/kata/is-that-a-real-phone-number-british-version/train/python

from unittest import TestCase
import re


def validate_number(string):
    messages = {
        True: "In with a chance",
        False: "Plenty more fish in the sea",
    }

    return messages[bool(re.match("^(\+447|07)\d{9}$", string.replace("-", "")))]


test = TestCase()
test.assertEqual(validate_number("07454876120"), "In with a chance")
test.assertEqual(validate_number("0754876120"), "Plenty more fish in the sea")
test.assertEqual(validate_number("0745--487-61-20"), "In with a chance")
test.assertEqual(validate_number("+447535514555"), "In with a chance")
test.assertEqual(validate_number("-07599-51-4555"), "In with a chance")
test.assertEqual(validate_number("075335440555"), "Plenty more fish in the sea")
test.assertEqual(validate_number("+337535512555"), "Plenty more fish in the sea")
test.assertEqual(validate_number("00535514555"), "Plenty more fish in the sea")
test.assertEqual(validate_number("+447+4435512555"), "Plenty more fish in the sea", "Not a Briish prefix")
test.assertEqual(validate_number("+44"), "Plenty more fish in the sea", "Not a Briish prefix")