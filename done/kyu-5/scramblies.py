# https://www.codewars.com/kata/scramblies/train/python

def scramble(s1, s2):
    def get_map(s):
        s = sorted(s)
        su = set(s)
        return {c: s.count(c) for c in su}
    s1u = get_map(s1)
    s2u = get_map(s2)
    for char in s2u.keys():
        if char not in s1u.keys(): return False
        if s2u[char] > s1u[char]: return False
    return True

# tests

import unittest


class PrimesWithMemoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(scramble('rkqodlw', 'world'))
        self.assertTrue(scramble('cedewaraaossoqqyt', 'codewars'))
        self.assertTrue(scramble('scriptjava', 'javascript'))
        self.assertTrue(scramble('scriptingjava', 'javascript'))

    def test_false(self):
        self.assertFalse(scramble('katas', 'steak'))

    def test_performance(self):
        level = 5
        s1 = ""
        for s in "zqwertyuiopasdfghjklxcvbnm": s1 += s * int(10 ** level)
        s1 += "z" * int(10 ** level * 2)
        s2 = ""
        for s in "zqwertyuiopasdfghjklxcvbnm": s2 += s * int(10 ** level)
        s2 += "z" * int(10 ** level * 2)
        actual = scramble(s1, s2)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
