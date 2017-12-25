# https://www.codewars.com/kata/simple-parenthesis-removal/train/python

import unittest


def solve(s):
    s = s.replace("(", "").replace(")", "")
    while "--" in s:
        s = s.replace("--", "+")

    while "+-" in s:
        s = s.replace("+-", "-")

    while "++" in s:
        s = s.replace("++", "+")

    if "+" == s[0]:
        s = s[1:]

    return s


class SimpleParanthesisRemovalTest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(solve("a-(b)"), "a-b")
        self.assertEqual(solve("a-(-b)"), "a+b")
        self.assertEqual(solve("a+(b)"), "a+b")
        self.assertEqual(solve("a+(-b)"), "a-b")

    def test_nested(self):
        self.assertEqual(solve("(((((((((-((-(((n))))))))))))))"), "n")
        self.assertEqual(solve("(((a-((((-(-(f)))))))))"), "a-f")
        self.assertEqual(solve("((((-(-(-(-(m-g))))))))"), "m-g")
        self.assertEqual(solve("(((((((m-(-(((((t)))))))))))))"), "m+t")
        self.assertEqual(solve("x-(-((-((((-((-(-(-y)))))))))))"), "x-y")

    def test_single_variable(self):
        self.assertEqual(solve("-x"), "-x")
        self.assertEqual(solve("-(-(x))"), "x")
        self.assertEqual(solve("-((-x))"), "x")
        self.assertEqual(solve("-(-(-x))"), "-x")

    def test_two_variables(self):
        self.assertEqual(solve("-(-(x-y))"), "x-y")
        self.assertEqual(solve("-(x-y)"), "-x+y")

    @unittest.skip("later")
    def test_three_variables(self):
        self.assertEqual(solve("x-(y+z)"), "x-y-z")
        self.assertEqual(solve("x-(y-z)"), "x-y+z")
        self.assertEqual(solve("x-(-y-z)"), "x+y+z")

    @unittest.skip("later")
    def test_many_variables(self):
        self.assertEqual(solve("u-(v-w+(x+y))-z"), "u-v+w-x-y-z")
        self.assertEqual(solve("x-(s-(y-z))-(a+b)"), "x-s+y-z-a-b")
        self.assertEqual(solve("u+(g+v)+(r+t)"), "u+g+v+r+t")
        self.assertEqual(solve("q+(s-(x-o))-(t-(w-a))"), "q+s-x+o-t+w-a")
        self.assertEqual(solve("u-(v-w-(x+y))-z"), "u-v+w+x+y-z")
        self.assertEqual(solve("v-(l+s)-(t+y)-(c+f)+(b-(n-p))"), "v-l-s-t-y-c-f+b-n+p")

if __name__ == '__main__':
    unittest.main()
