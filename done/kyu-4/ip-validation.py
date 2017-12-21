# https://www.codewars.com/kata/ip-validation/train/python

import unittest

def is_valid_IP(strng):
    import re
    part_pattern = "([0-9]|[1-9][0-9]|1[0-9][0-9]|2([0-4][0-9]|5[0-5]))"
    pattern = "^" + "\.".join([part_pattern] * 4) + "$"
    return bool(re.match(pattern, strng))

class IpValidationTest(unittest.TestCase):

    def test_full_valid(self):
        self.assertTrue(is_valid_IP('12.255.56.1'))
        self.assertTrue(is_valid_IP('127.1.1.0'))
        self.assertTrue(is_valid_IP('0.0.0.0'))
        self.assertTrue(is_valid_IP('0.34.82.53'))


    def test_full_invalid(self):
        self.assertFalse(is_valid_IP(''))
        self.assertFalse(is_valid_IP('abc.def.ghi.jkl'))
        self.assertFalse(is_valid_IP('123.456.789.0'))
        self.assertFalse(is_valid_IP('12.34.56'))
        self.assertFalse(is_valid_IP('12.34.56 .1'))
        self.assertFalse(is_valid_IP('12.34.56.-1'))
        self.assertFalse(is_valid_IP('123.045.067.089'))
        self.assertFalse(is_valid_IP('192.168.1.300'))
        self.assertFalse(is_valid_IP("256.1.2.3'"))


if __name__ == '__main__':
    unittest.main()
