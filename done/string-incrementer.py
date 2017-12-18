# https://www.codewars.com/kata/string-incrementer/train/python

from unittest import TestCase
import re


def search(s):
    return re.search("(\d*)$", s)


def head(s):
    if s == "":
        return ""

    return s.rstrip(tail(s))


def tail(s):
    return search(s).group()


def incremented_tail(s):
    t = tail(s)
    if t == "":
        return "1"

    l = len(t)
    t = str(int(t) + 1)
    h = "0" * (l - len(t))

    return h + t


def increment_string(strng):
    return head(strng) + incremented_tail(strng)


class TestData(object):
    def __init__(self, value, head, tail, incremented_tail, increment_string):
        self.value = value
        self.head = head
        self.tail = tail
        self.incremented_tail = incremented_tail
        self.increment_string = increment_string


test_data = [
    TestData("foo", "foo", "", "1", "foo1"),
    TestData("foobar001", "foobar", "001", "002", "foobar002"),
    TestData("foobar1", "foobar", "1", "2", "foobar2"),
    TestData("foobar00", "foobar", "00", "01", "foobar01"),
    TestData("foobar99", "foobar", "99", "100","foobar100"),
    TestData("foobar099", "foobar", "099", "100", "foobar100"),
    TestData("", "", "", "1", "1"),
    TestData("foobar00999", "foobar", "00999", "01000", "foobar01000"),
    TestData("1", "", "1", "2", "2"),
    TestData(")sn5[208711#Js93212757005331456479",
             ")sn5[208711#Js", "93212757005331456479", "93212757005331456480",
             ")sn5[208711#Js93212757005331456480"),
    TestData("2cG:Ks0\"MA4d]71706Ov_{o%%9124?c5'0827202~1dr|YM7X036688000000008242301",
        "2cG:Ks0\"MA4d]71706Ov_{o%%9124?c5'0827202~1dr|YM7X",
        "036688000000008242301",
        "036688000000008242302",
        "2cG:Ks0\"MA4d]71706Ov_{o%%9124?c5'0827202~1dr|YM7X036688000000008242302")
]
test = TestCase()
for data in test_data:
    test.assertEqual(head(data.value), data.head)
    test.assertEqual(tail(data.value), data.tail)
    test.assertEqual(incremented_tail(data.value), data.incremented_tail)
    test.assertEqual(increment_string(data.value), data.increment_string)



