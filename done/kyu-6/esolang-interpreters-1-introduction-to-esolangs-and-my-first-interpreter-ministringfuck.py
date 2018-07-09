# https://www.codewars.com/kata/esolang-interpreters-number-1-introduction-to-esolangs-and-my-first-interpreter-ministringfuck/train/python

def my_first_interpreter(code):
    output = ''
    pointer = 0

    for command in code:
        if command == '+':
            pointer = (pointer + 1) % 256
            continue

        if command == '.':
            output += chr(pointer)
            continue

    return output


print(my_first_interpreter(('+' * 72) + '.' + ('+' * 29) + '.' + ('+' * 7)
    + '..' + ('+' * 3) + '.' + ('+' * 189) + '.' + ('+' * 244) + '.' + ('+' * 55)
    + '.' + ('+' * 24) + '.' + ('+' * 3) + '.' + ('+' * 250) + '.' + ('+' * 248)
    + '.' + ('+' * 189)))


# test.assert_equals(solution(
#     '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.'),
#                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
