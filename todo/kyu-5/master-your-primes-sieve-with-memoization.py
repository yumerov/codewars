# https://www.codewars.com/kata/master-your-primes-sieve-with-memoization/train/python

primes = [2, 3, 5, 7]
def is_prime(n):
    if n in primes:
        return n

    if n < 2:
        return False
    for prime in range(2, n):
        if prime in primes:
            continue

        for i in range(4, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

# tests

import unittest


class PrimesWithMemoTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertTrue(abs(len(primes) - 5) < 3)
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(53))
        self.assertTrue(abs(len(primes) - 9) < 3)

    def test_false(self):
        self.assertFalse(is_prime(529))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-1),)
        self.assertFalse(is_prime(143))
if __name__ == '__main__':
    unittest.main()
