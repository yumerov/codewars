# https://www.codewars.com/kata/valid-braces/train/python

class Brace(object):
    open_braces = ["(", "{", "["]
    close_braces = [")", "}", "]"]
    opposite_braces = {
        ")": "(",
        "(": ")",
        "}": "{",
        "{": "}",
        "]": "[",
        "[": "]",
    }
    def __init__(self, brace):
        self.brace = brace
    def is_open(self):
        return self.brace in self.open_braces

    def is_close(self):
        return self.brace in self.close_braces

    def is_opposite_of(self, opposite):
        return self.opposite_braces[self.brace] == opposite

class Solution(object):
    def __init__(self, string):
        self.string = string

    def solve(self):
        open_braces = []
        for character in self.string:
            if Brace(character).is_open():
                open_braces.append(character)
                continue

            if open_braces == []:
                continue

            if Brace(character).is_opposite_of(open_braces[-1]):
                open_braces = open_braces[:-1]
            else:
                return False

        return len(open_braces) == 0



def validBraces(string):
    return Solution(string).solve()


import unittest


class ValidBracesTest(unittest.TestCase):
    def test_small_valid(self):
        self.assertTrue(validBraces("()"))

    def test_small_invalid(self):
        self.assertFalse(validBraces("[(])"))

    def test_with_complex(self):
        self.assertFalse(validBraces("(((({{"))


if __name__ == '__main__':
    unittest.main()
