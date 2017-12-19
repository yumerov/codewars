# https://www.codewars.com/kata/your-order-please/train/python

import re


def extract(word):
    return int(re.search('(\d)', word).group())


def order(sentence):
    if sentence == "":
        return ""
    words = sentence.split(" ")
    print(words)
    d = {}
    for word in words:
        d[extract(word)] = word
    print(d)
    t = lambda index: d[index]
    return " ".join(list(map(t, sorted(d.keys()))))

print(order("is2 Thi1s T4est 3a"))