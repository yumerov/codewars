# https://www.codewars.com/kata/python-checkerboard/train/python

from unittest import TestCase
import math


def generate_row(size):
    return ['X', 'O'] * math.ceil((size + 1) / 2)

def slide_row(row, row_index, size):
    left = row_index % 2
    return row[left:left + size]


def make_checkered_board(n):
    row = generate_row(n)
    return [slide_row(row, i, n) for i in range(n)]

test = TestCase()
test.assertEqual(
    make_checkered_board(5),
    [['X', 'O', 'X', 'O', 'X'],
    ['O', 'X', 'O', 'X', 'O'],
    ['X', 'O', 'X', 'O', 'X'],
    ['O', 'X', 'O', 'X', 'O'],
    ['X', 'O', 'X', 'O', 'X']])

test.assertEqual(
    make_checkered_board(6),
    [['X', 'O', 'X', 'O', 'X', 'O'],
     ['O', 'X', 'O', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'O', 'X', 'O'],
     ['O', 'X', 'O', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'O', 'X', 'O'],
     ['O', 'X', 'O', 'X', 'O', 'X']])