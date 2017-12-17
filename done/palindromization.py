# https://www.codewars.com/kata/palindromization/train/python

from unittest import TestCase


def left(e, n):
    l = len(e)
    ll = n // 2 # left length
    h = e * (ll // l) # head
    t = e[:ll % l]
    return h + t


def mid(e, n):
    l = len(e)
    ll = n // 2
    i = (ll) % l
    return e[i] * (n % 2)


def palindromization(e, n):
    if len(e) < 1 or n < 2:
        return "Error!"
    return left(e, n) + mid(e, n) + left(e, n)[::-1]


test = TestCase()
test.assertEqual(left("123", 2), "1")
test.assertEqual(mid("123", 2), "")
test.assertEqual(palindromization("123", 2), "11")

test.assertEqual(left("123", 3), "1")
test.assertEqual(mid("123", 3), "2")
test.assertEqual(palindromization("123", 3), "121")

test.assertEqual(left("123", 4), "12",)
test.assertEqual(mid("123", 4), "")
test.assertEqual(palindromization("123", 4), "1221")

test.assertEqual(left("123", 5), "12")
test.assertEqual(mid("123", 5), "3")
test.assertEqual(palindromization("123", 5), "12321")

test.assertEqual(left("123", 6), "123")
test.assertEqual(mid("123", 6), "")
test.assertEqual(palindromization("123", 6), "123321")

test.assertEqual(left("123", 7), "123")
test.assertEqual(mid("123", 7), "1")
test.assertEqual(palindromization("123", 7), "1231321")

test.assertEqual(left("123", 8), "1231")
test.assertEqual(mid("123", 8), "")
test.assertEqual(palindromization("123", 8), "12311321")

test.assertEqual(left("123", 9), "1231")
test.assertEqual(mid("123", 9), "2")
test.assertEqual(palindromization("123", 9), "123121321")

test.assertEqual(left("123", 10), "12312")
test.assertEqual(mid("123", 10), "")
test.assertEqual(palindromization("123", 10), "1231221321")

test.assertEqual(palindromization("", 2), "Error!")
test.assertEqual(palindromization("123", 1), "Error!")
