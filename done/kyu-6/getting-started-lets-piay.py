# https://www.codewars.com/kata/getting-started-number-lets-piay/train/python

from math import pi

def get_map(alpha):
    # create a dictionary linking alphabet to 'secret encryption'
    # {85:'a', 24:'b',32:'c', [...],10:'z'}
    keys = [85, 24, 32, 64, 11, 52, 91, 79, 78, 99, 62, 27, 74, 35, 14, \
            16, 66, 81, 19, 39, 13, 33, 45, 49, 95, 10]
    return dict(zip(keys, alpha.upper()))

def get_code(crypt):
    code = []
    # reverse the string and group 2 by 2 to form a list
    for i in range(0, len(crypt), 2):
        print(crypt[::-1][i:i + 2])
        code.append(int(crypt[::-1][i:i + 2]))
    return code

def get_decrypt(code, dico):
    # take the modified string and try to decode
    decrypt = ''
    for binom in code:
        decrypt += dico[binom]

    return decrypt


def whatpimeans(alpha = 'abcdefghijklmnopqrstuvwxyz'):
    dico = get_map(alpha)
    code = get_code(str(pi).replace('.', ''))
    return get_decrypt(code, dico)

print(whatpimeans())