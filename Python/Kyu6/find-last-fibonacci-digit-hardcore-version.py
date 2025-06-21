# https://www.codewars.com/kata/find-last-fibonacci-digit-hardcore-version/train/python


from unittest import TestCase

def last_fib_digit(n):
    if n in [1, 2]:
        return 1

    a = 1
    b = 1
    counter = 3
    n %= 60
    while counter <= n:
        a, b = b % 10, (a + b) % 10
        counter += 1

    return b


test = TestCase()
test.assertEqual(last_fib_digit(1), 1)
test.assertEqual(last_fib_digit(21), 6)
test.assertEqual(last_fib_digit(302), 1)
test.assertEqual(last_fib_digit(4003), 7)
test.assertEqual(last_fib_digit(50004), 8)
test.assertEqual(last_fib_digit(600005), 5)
test.assertEqual(last_fib_digit(7000006), 3)
test.assertEqual(last_fib_digit(80000007), 8)
test.assertEqual(last_fib_digit(900000008), 1)
test.assertEqual(last_fib_digit(1000000009), 9)
