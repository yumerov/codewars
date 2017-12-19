# https://www.codewars.com/kata/bug-fix-quick-sort/train/python

import unittest


def quicksort(arr):
    if len(arr) < 2: return arr
    p = arr[0]
    head = quicksort(map(lambda x: x < p, arr[::-1]))
    tail = quicksort(map(lambda x: x > p, arr[1:]))
    return head + tail


class TestSolution(unittest.TestCase):
    def test_single_item_list(self):
        self.assertEqual(quicksort([1]), [1])

    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_small_list_with_positive_numbers(self):
        self.assertEqual(quicksort([1, 5, 2]), [1, 2, 5])

        # def test_small_list_with_negative_numbers(self):
        #     self.assertEqual(quicksort([17, -5, 3]), [-5, 3, 17])
        #
        # def test_with_ten_values(self):
        #     inpt = [3, 0, 7, 5, 1, 2, 9, 8, 4, 6]
        #     expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #     self.assertEqual(quicksort(inpt),expected)


if __name__ == '__main__':
    unittest.main()
