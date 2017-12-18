# https://www.codewars.com/kata/goldbachs-conjecture-1/train/python

from unittest import TestCase

primes = set()

def is_prime(num):
    if num in primes:
        return True

    for i in range(2, num):
        if (num % i) == 0: return False

    primes.add(num)
    return True


def goldbach_partitions(n):
    if n % 2 == 1 or n <= 2 or n > 32000:
        return []

    partitions = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            partitions.append("{}+{}".format(i, n- i))

    return partitions

test = TestCase()
test.assertEqual(goldbach_partitions(4), ['2+2'])
test.assertEqual(goldbach_partitions(7), [])
test.assertEqual(goldbach_partitions(26), ['3+23', '7+19', '13+13'])
test.assertEqual(goldbach_partitions(100), ['3+97', '11+89', '17+83',
                                            '29+71', '41+59', '47+53'])