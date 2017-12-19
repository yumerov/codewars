# https://www.codewars.com/kata/pythons-dynamic-classes-number-1/train/python

from unittest import TestCase


def class_name_changer(cls, new_name):
    cls.__class__ = type(new_name, (object, ), {})
    return cls


# tests

class MyClass(object):
    def __str__(self):
        return str(type(self))


myObject = MyClass()
test = TestCase()
test.assertEqual(str(MyClass), "<class '__main__.MyClass'>",
                 "Original class name shouldn't be changed yet...")

class_name_changer(MyClass, "UsefulClass")
test.assertEqual(str(MyClass), "<class '__main__.UsefulClass'>",
                 "New class name should be as boss wanted to!")

class_name_changer(MyClass, "SecondUsefulClass")
test.assertEqual(str(MyClass), "<class '__main__.SecondUsefulClass'>",
                 "New class name should be as boss wanted to!")
