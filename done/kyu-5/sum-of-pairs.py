# https://www.codewars.com/kata/sum-of-pairs/train/python


def purge_ints(ints):
    purged = []
    for i in range(len(ints) - 2):
        if ints[i] == ints[i + 1] and ints[i + 1] == ints[i + 2]:
            continue
        purged.append(ints[i])
    purged.append(ints[-2])
    purged.append(ints[-1])
    return purged


def sum_pairs(ints, s):
    ints = purge_ints(ints)
    l = len(ints)
    pairs = {}
    for i in range(l - 1):
        for j in range(i + 1, l):
            a, b = ints[i], ints[j]
            if a + b == s:
                pairs[(i + j) / 2] = [a, b]

    keys = pairs.keys()
    return pairs[min(keys)] if keys != [] else None

# tests

import unittest


class SumOfPairsTest(unittest.TestCase):
    def test_purge(self):
        l0 = [13, 1, 1, 1, 1, 1]
        self.assertEqual(purge_ints(l0), [13, 1, 1])

    def test_simple(self):
        l1 = [1, 4, 8, 7, 3, 15]
        self.assertEqual(sum_pairs(l1, 8), [1, 7])

    def test_negative(self):
        l2 = [1, -2, 3, 0, -6, 1]
        self.assertEqual(sum_pairs(l2, -6), [0, -6])

    def test_none(self):
        l3 = [20, -13, 40]
        self.assertEqual(sum_pairs(l3, -7), None)

    def test_first_match_from_left(self):
        l4 = [1, 2, 3, 4, 1, 0]
        self.assertEqual(sum_pairs(l4, 2), [1, 1])

    def test_first_match_from_left_redux(self):
        l5 = [10, 5, 2, 3, 7, 5]
        self.assertEqual(sum_pairs(l5, 10), [3, 7])

    def test_duplicates(self):
        l6 = [4, -2, 3, 3, 4]
        self.assertEqual(sum_pairs(l6, 8), [4, 4])

    def test_zeroes(self):
        l7 = [0, 2, 0]
        self.assertEqual(sum_pairs(l7, 0), [0, 0])

    def test_substraction(self):
        l8 = [5, 9, 13, -3]
        self.assertEqual(sum_pairs(l8, 10), [13, -3])

    def test_long_list(self):
        l9 = [13] + [1] * 5000
        self.assertEqual(sum_pairs(l9, 14), [13, 1])

if __name__ == '__main__':
    unittest.main()
