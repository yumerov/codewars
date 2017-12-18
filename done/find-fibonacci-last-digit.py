# https://www.codewars.com/kata/round-and-round/train/python


from unittest import TestCase

def get_last_digit(n):
    if n  in [1, 2]:
        return 1

    a = 1
    b = 1
    counter = 3
    while counter <= n:
        a, b = b % 10, (a + b) % 10
        counter += 1

    return b


for i in range(1, 100):
    print(get_last_digit(i))

test = TestCase()
test.assertEqual(get_last_digit(1), 1)
test.assertEqual(get_last_digit(2), 1)
test.assertEqual(get_last_digit(3), 2)

test.assertEqual(get_last_digit(193150), 5)
test.assertEqual(get_last_digit(300), 0)
test.assertEqual(get_last_digit(20001), 6)
test.assertEqual(get_last_digit(800), 5)
test.assertEqual(get_last_digit(1001), 1)
test.assertEqual(get_last_digit(100), 5)
test.assertEqual(get_last_digit(260), 5)
test.assertEqual(get_last_digit(1111), 9)
test.assertEqual(get_last_digit(1234), 7)
test.assertEqual(get_last_digit(99999), 6)
test.assertEqual(get_last_digit(10), 5)
test.assertEqual(get_last_digit(234), 2)
test.assertEqual(get_last_digit(193241), 1)
test.assertEqual(get_last_digit(79), 1)
test.assertEqual(get_last_digit(270), 0)