# https://www.codewars.com/kata/linux-history-and-%60-%60-command-series-number-4-the-%60-string%60-command/train/python


from unittest import TestCase


def get_command_lines(history):
    commands = history.split("\n")
    return list(map(lambda x: x.strip().lstrip("0123456789").strip(), commands))

def bang_start_string(n, history):
    commands = get_command_lines(history)
    for command in commands[::-1]:
        if command.startswith(n):
            return command
    return "!{}: event not found".format(n)


test = TestCase()
history = "   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me \n  7  more me\n  8  history"
test.assertEqual(bang_start_string("more", history), "more me")
history = "   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me \n  7  history\n  8  more me"
test.assertEqual(bang_start_string("touch", history), "touch me")
test.assertEqual(bang_start_string("mkdir", history), "!mkdir: event not found")
