# https://www.codewars.com/kata/directions-reduction/train/python
from unittest import TestCase


def convert(color):
    color = 0 if color < 0 else 255 if color > 255 else color
    prefix = "0" if color <= 10 else ""
    return prefix + hex(color).replace("0x", "").upper()


def rgb(r, g, b): return convert(r) + convert(g) + convert(b)


test = TestCase()
test.assertEqual(rgb(0,0,0),"000000", "testing zero values")
test.assertEqual(rgb(1,2,3),"010203", "testing near zero values")
test.assertEqual(rgb(255,255,255), "FFFFFF", "testing max values")
test.assertEqual(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assertEqual(rgb(-20,275,125), "00FF7D", "testing out of range values")