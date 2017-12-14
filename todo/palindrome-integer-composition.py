# https://www.codewars.com/kata/palindrome-integer-composition/train/python
from unittest import TestCase


def get_palindromes(n): return list(filter(lambda x: x == int(str(x)[::-1]), list(range(2, n + 1))))

def sum_of_squares(n): return n * (n + 1) * (2 * n + 1) / 6

def sum_of_squares_between(a, b): return sum_of_squares(b) - sum_of_squares(a - 1)

def is_sum_of_squares_of_consecutive_numbers(palindrome):
    upper_limit = int(palindrome ** 0.5) + 1
    for start in range(1, upper_limit):
        lower_limit = start + 1
        end = int((lower_limit + upper_limit) / 2)
        while end != lower_limit and end != upper_limit:
            l = list(range(start, end + 1))
            print("pali: {}\nlimit:{}\nlen:{}\nseq:{}\n".format(palindrome,
                                                                upper_limit, len(l), l))
            s = sum_of_squares_between(start, end)
            if palindrome > s:
                end = int((end + upper_limit) / 2) + 1
                continue
            elif palindrome == s:
                print(">>>>")
                return True
            else:
                end = int((lower_limit + end) / 2) + 1
                continue

        # for end in range(start + 1, upper_limit):
        #     s = sum_of_squares_between(start, end)
        #
        #     if palindrome > s:
        #         # l = list(range(start, end + 1))
        #         # print("{}[{}] [{}]{}".format(palindrome, upper_limit, len(l), l))
        #         continue
        #     elif palindrome == s:
        #         l = list(range(start, end + 1))
        #         print("pali: {}\nlimit:{}\nlen:{}\nseq:{}\n".format(palindrome, upper_limit, len(l), l))
        #         # print("{} {}".format(palindrome, l))
        #         return True
        #     else:
        #         break


def values(n):
    palindromes = get_palindromes(n)
    palindromes_sum_of_squares = filter(is_sum_of_squares_of_consecutive_numbers, palindromes)
    return len(list(palindromes_sum_of_squares))


test = TestCase()
print("Small values")
test.assertEqual(values(100),3)
# test.assertEqual(values(200),4)
# test.assertEqual(values(300),4)
# test.assertEqual(values(400),5)
# test.assertEqual(values(100000),30)

# print("large values")
# test.assertEqual(values(1000000),59)
# test.assertEqual(values(5000000),78)
# test.assertEqual(values(9000000),98)
# test.assertEqual(values(10000000),110)
