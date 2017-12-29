# https://www.codewars.com/kata/string-character-frequency/train/python

def solve(s):
    print(s)
    m = {x: s.count(x) for x in set(s)}
    l = len(m.keys())
    if l == 1 or sum(m.values()) == l:
        return True

    vs = sorted(m.values())
    if min(vs) == 1 and vs.count(1) == 1:
        return True

    return max(vs) - min(vs) == 1


# tests

import unittest


class CharacterFrequencyTest(unittest.TestCase):

    def test_true(self):
        data = ['aaaa', 'abbba', 'aabbccddd', 'aabcde', 'abcde']
        for s in data:
            self.assertTrue(solve(s), msg="failed with '{}'".format(s))


    def test_false(self):
        data = ['abba', 'aabbcc', 'aaaabb', 'aaabcde', 'abbccc']
        for s in data:
            self.assertFalse(solve(s), msg="failed with '{}'".format(s))

    def test_random_false(self):
        self.assertFalse(solve("aaabcde"))

if __name__ == '__main__':
    unittest.main()
