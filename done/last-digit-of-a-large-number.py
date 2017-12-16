# http://www.codewars.com/kata/last-digit-of-a-large-number/train/python


from unittest import TestCase

repeat_map = {
    0: [0],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    digit = n1 % 10
    possible_last_digits = repeat_map[digit]
    return repeat_map[digit][n2  % len(possible_last_digits) - 1]



test = TestCase()
test.assertEqual(last_digit(4, 1), 4)
test.assertEqual(last_digit(4, 2), 6)
test.assertEqual(last_digit(9, 7), 9)
test.assertEqual(last_digit(10, 10 ** 10), 0)
test.assertEqual(last_digit(2 ** 200, 2 ** 300), 6)
test.assertEqual(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)