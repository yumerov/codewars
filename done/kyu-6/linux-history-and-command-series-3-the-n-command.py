# https://www.codewars.com/kata/linux-history-and-%60-%60-command-series-number-3-the-%60-n%60-command/train/python


from unittest import TestCase


def strip_command(command):
    return command.strip().lstrip("0123456789").strip()

def get_command_lines(history):
    commands = history.split("\n")
    return list(map(strip_command, commands))[::-1]

def bang_minus_n(n, history):
    commands = get_command_lines(history)

    if n <= len(commands):
        return commands[n - 1]
    return "!-{}: event not found".format(n)


test = TestCase()
history="   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me \n  7  more me\n  8  history"
test.assertEqual(bang_minus_n(4,history), "touch me")
history="   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls\n  5  touch me\n  6  chmod 000 me \n  7  history\n  8  more me"
test.assertEqual(bang_minus_n(2,history), "history")
test.assertEqual(bang_minus_n(12,history), "!-12: event not found")
