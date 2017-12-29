# https://www.codewars.com/kata/first-n-prime-numbers/train/python

class Primes:
    primes = [2, 3, 5]
    @staticmethod
    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i: return False
        return True

    @staticmethod
    def next_prime(n):
        while True:
            n += 1
            if Primes.is_prime(n): return n

    @staticmethod
    def first(n):
        l = len(Primes.primes)
        if n < l:
            return Primes.primes[:n]
        for i in range(l, n):
            Primes.primes.append(Primes.next_prime(Primes.primes[-1]))
        return Primes.primes



# tests

import unittest


class VectorClassSimpleTest(unittest.TestCase):
    def test_simple(self):
        # self.assertEqual(Primes.first(1), [2])
        # self.assertEqual(Primes.first(2), [2, 3])
        self.assertEqual(Primes.first(5), [2, 3, 5, 7, 11])
        # self.assertEqual(Primes.first(20)[-5:], [53, 59, 61, 67, 71])
        # self.assertEqual(Primes.first(100)[99], 541)
        # self.assertEqual(Primes.first(80)[79], 409)

if __name__ == '__main__':
    unittest.main()
