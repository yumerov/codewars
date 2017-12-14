# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/python

def digital_root(n):
    s = sum(list(map(lambda x: int(x), str(n))))
    if s < 10: return s
    else: return digital_root(s)

print(digital_root(9998))