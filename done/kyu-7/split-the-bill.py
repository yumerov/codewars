# https://www.codewars.com/kata/split-the-bill/train/python


def split_the_bill(b):
    l = len(b.keys())
    s = sum(list(map(lambda k: b[k], b)))
    split = {}
    for key in b.keys():
        split[key] = round(b[key] - float(s) / l, 2)
    return split

def t(i, e):
    a = split_the_bill(i)
    if a != e:
        raise Exception("{} should be equal {}".format(a, e))
t({'A': 20, 'B': 15, 'C': 10}, {'A': 5, 'B': 0, 'C': -5})
t({'A': 40, 'B': 25, 'X': 10}, {'A': 15, 'B': 0, 'X': -15})
t({'A': 40, 'C': 10, 'B': 25, 'E': 58, 'D': 153}, {'A': -17.2, 'C': -47.2, 'B': -32.2, 'E': 0.8, 'D': 95.8})