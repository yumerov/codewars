# https://www.codewars.com/kata/last-digits-of-n-2-equals-equals-n/train/python

from unittest import TestCase

def is_green(n):
    return str(n ** 2).endswith(str(n))

def green(n):
    i = 1
    j = 1
    while i <= n:
        while True:
            print(j)
            if is_green(j):
                break
            j += 1
        i += 1
    return j


# test
test = TestCase()

test.assertEqual(is_green(2), False)
test.assertEqual(is_green(5), True)
test.assertEqual(is_green(376), True)

test.assertEqual(green(1), 1)
test.assertEqual(green(2), 5)
test.assertEqual(green(3), 6)
test.assertEqual(green(4), 25)

# test.assertEqual(green(12), 2890625)
# test.assertEqual(green(13), 7109376)

# test.assertEqual(green(100), 6188999442576576769103890995893380022607743740081787109376)
# test.assertEqual(green(110),
#     9580863811000557423423230896109004106619977392256259918212890625)
