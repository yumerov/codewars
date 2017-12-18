# https://www.codewars.com/kata/pairing-brackets/train/python


from unittest import TestCase

def is_bracket(char):
    return is_open_bracket(char) or is_closing_bracket(char)

def is_open_bracket(char):
    return char == "("

def is_closing_bracket(char):
    return char == ")"


def first_open_bracket(brackets):
    for start in list(brackets.keys())[::-1]:
        if brackets[start] == None:
            return start
    return None

def bracket_pairs(s):
    brackets = {}
    for index in range(0, len(s)):
        current = s[index]
        if not is_bracket(current):
            continue

        if is_open_bracket(current):
            brackets[index] = None
            continue

        if is_closing_bracket(current):
            open_bracket = first_open_bracket(brackets)
            if open_bracket is None:
                return False
            brackets[open_bracket] = index
    if first_open_bracket(brackets) is not None:
        return False
    return brackets

test = TestCase()
test.assertEqual(bracket_pairs("len(list)"), {3: 8}, "Single pair of brackets")
test.assertEqual(bracket_pairs("def f(x"), False, "unmatched bracket")
test.assertEqual(bracket_pairs("(a(b)c()d)"), {0: 9, 2: 4, 6: 7}, "nested "
                                                                  "brackets")
