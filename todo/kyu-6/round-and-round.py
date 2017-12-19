# https://www.codewars.com/kata/round-and-round/train/python

from decimal import Decimal
from unittest import TestCase


def round_by_2_decimal_places(n):
    return Decimal(round(round(n * 100, 2) / 100, 2))


test = TestCase()
test.assertEqual(round_by_2_decimal_places(Decimal('2')), Decimal('2'))
test.assertEqual(round_by_2_decimal_places(Decimal('7.477')), Decimal('7.48'))
test.assertEqual(round_by_2_decimal_places(Decimal('-4.999')), Decimal('-5'))
test.assertEqual(round_by_2_decimal_places(Decimal('18.123')), Decimal('18.12'))
test.assertEqual(round_by_2_decimal_places(Decimal('0')), Decimal('0'))
test.assertEqual(round_by_2_decimal_places(Decimal('1.455')), Decimal('1.46'))
test.assertEqual(round_by_2_decimal_places(Decimal('-1.455')), Decimal('-1.46'))
test.assertEqual(round_by_2_decimal_places(Decimal('1.055')), Decimal('1.06'))
test.assertEqual(round_by_2_decimal_places(Decimal('-1.055')), Decimal('-1.06'))
test.assertEqual(round_by_2_decimal_places(Decimal('16.765')), Decimal('16.77'))
test.assertEqual(round_by_2_decimal_places(Decimal('-16.765')), Decimal('-16.77'))
test.assertEqual(round_by_2_decimal_places(Decimal('1.025')), Decimal('1.03'))
test.assertEqual(round_by_2_decimal_places(Decimal('-1.025')), Decimal('-1.03'))
test.assertEqual(round_by_2_decimal_places(Decimal('16.355')), Decimal('16.36'))
test.assertEqual(round_by_2_decimal_places(Decimal('-16.345')), Decimal('-16.35'))
test.assertEqual(round_by_2_decimal_places(Decimal('-1.1949999999999999999999999999')), Decimal('-1.19'))
test.assertEqual(round_by_2_decimal_places(Decimal('-1.1950000000000000000000000001')), Decimal('-1.2'))
test.assertEqual(round_by_2_decimal_places(Decimal('1.1949999999999999999999999999')), Decimal('1.19'))
test.assertEqual(round_by_2_decimal_places(Decimal('1.1950000000000000000000000001')), Decimal('1.2'))
test.assertEqual(round_by_2_decimal_places(Decimal('-1.1849999999999999999999999999')), Decimal('-1.18'))
test.assertEqual(round_by_2_decimal_places(Decimal('-1.1850000000000000000000000001')), Decimal('-1.19'))
test.assertEqual(round_by_2_decimal_places(Decimal('1.1849999999999999999999999999')), Decimal('1.18'))
test.assertEqual(round_by_2_decimal_places(Decimal('1.1850000000000000000000000001')), Decimal('1.19'))