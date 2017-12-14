# https://www.codewars.com/kata/moving-zeros-to-the-end/train/python

from numbers import Number

def is_zero(zero):
    if isinstance(zero, Number):
        return str(zero) != '0' and str(zero) != '0.0'
    return True

def move_zeros(array):
    purged = [x for x in array if is_zero(x)]
    return purged + (len(array) - len(purged)) * [0]
