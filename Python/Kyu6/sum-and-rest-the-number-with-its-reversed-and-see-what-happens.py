# https://www.codewars.com/kata/sum-and-rest-the-number-with-its-reversed-and-see-what-happens/train/python

cache = {}
def sum_dif_rev(n):
    if n in cache.keys():
        return cache[n]

    value = 1
    for i in range(1, n + 1):

        while True:
            value += 1
            if str(value)[-1] == "0":
                continue
            reverse = int(str(value)[::-1])
            if value == reverse:
                continue

            if (value + reverse) % abs(value - reverse) == 0:
                cache[i] = value
                break
    return value


# tests
import unittest


class CountAliveNeighborsTest(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(sum_dif_rev(1), 45)
        self.assertEqual(sum_dif_rev(2), 54)
        self.assertEqual(sum_dif_rev(3), 495)
        self.assertEqual(sum_dif_rev(4), 594)
        self.assertEqual(sum_dif_rev(5), 4356)
        self.assertEqual(sum_dif_rev(6), 4545)
        self.assertEqual(sum_dif_rev(7), 4995)
        self.assertEqual(sum_dif_rev(8), 5454)

for i in range(1, 31):
    v = sum_dif_rev(i)
    s = int(str(v)[::-1])
    print(i, v, s, s / 9, v / 9)

if __name__ == '__main__':
    unittest.main()