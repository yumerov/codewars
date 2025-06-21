import string
from codecs import encode as _dont_use_this_


def rot13(message):
    letters = list(map(lambda x: chr(x), range(ord('a'), ord('z') + 1)))
    rotted_letters = letters[13:] + letters[:13]
    rot_map = dict(zip(letters, rotted_letters))
    rot_map_upper = dict(zip(map(lambda x: x.upper(), letters), map(lambda x: x.upper(), rotted_letters)))
    rot_map_all_cases = dict(rot_map, **rot_map_upper)
    transform = lambda x: rot_map_all_cases[x] if x in rot_map_all_cases.keys() else x
    return "".join(map(transform, message))


print(rot13("Test"))

