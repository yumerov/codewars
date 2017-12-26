# https://www.codewars.com/kata/prime-sextuplets/train/python

primes = [2, 3, 5 ,7]
non_primes = []

def is_prime(n):
    if n in primes: return True

    if n in non_primes: return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            non_primes.append(n)
            return False

    primes.append(n)
    return True

def next_prime(n):
    if is_prime(n): return n

    while True:
        n += 1
        if is_prime(n): return n

def get_min_possible_prime(sum_limit): return sum_limit // 6 - 8

def possible_prime_sextuple(start):
    d = [0, 4, 6, 10, 12, 16]
    return [start + i for i in d]

def is_prime_sextuplets(sextuple):
    return len(filter(is_prime, sextuple)) == 6

def find_primes_sextuplet(sum_limit):
    start = next_prime(get_min_possible_prime(sum_limit))
    while True:
        sextuple = possible_prime_sextuple(start)
        if is_prime_sextuplets(sextuple):
            return sextuple
        start += 1


# tests
import unittest


class PrimeSextupletsTest(unittest.TestCase):
    def test_simple(self):
        actual = find_primes_sextuplet(70)
        expected = [7, 11, 13, 17, 19, 23]
        self.assertEqual(actual, expected)

    def test_advanced(self):
        actual = find_primes_sextuplet(600)
        expected = [97, 101, 103, 107, 109, 113]
        self.assertEqual(actual, expected)

    def test_performance(self):
        actual = find_primes_sextuplet(2000000)
        expected = [1091257, 1091261, 1091263, 1091267, 1091269,
                        1091273]
        self.assertFalse(actual, expected)
if __name__ == '__main__':
    unittest.main()